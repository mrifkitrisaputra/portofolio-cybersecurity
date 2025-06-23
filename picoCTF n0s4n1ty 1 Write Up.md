##  CTF Name: PIE TIME (Easy)

### Description:
A developer has added profile picture upload functionality to a website. However, the implementation is flawed, and it presents an opportunity for you. Your mission, should you choose to accept it, is to navigate to the provided web page and locate the file upload area. Your ultimate goal is to find the hidden flag located in the `/root` directory.

### Hint:
1. File upload was not sanitized
2. Whenever you get a shell on a remote machine, check `sudo -l`

### Analysis:
This challenge demonstrates a common backend misconfiguration: the file upload form accepts files without filtering by type or extension, allowing the attacker to upload a simple PHP web shell. By accessing the uploaded shell via the browser, we gain remote code execution on the server. Once inside, we find that the `www-data` user has `sudo` privileges with `NOPASSWD`, meaning we can escalate privileges without needing a password and directly read the root-only flag file.

### Solution:
1. **Create and upload a PHP web shell:**
Example shell code:
 ``
``
![f]()
2. **Access the shell and run commands:**
``http://.../uploads/shell.php?cmd=id``
![f]()

3. **Check sudo privileges:**
``?cmd=sudo -l
``
![f]()
4. **Read the flag:**
``?cmd=sudo ls /root
`` 
``?cmd=sudo cat /root/flag.txt
``
![f]()
![f]()


### Flag:
**picoCTF{wh47_c4n_u_d0_wPHP_f7424fc7}**
