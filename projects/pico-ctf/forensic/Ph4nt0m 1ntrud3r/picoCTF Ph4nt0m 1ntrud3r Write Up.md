##  CTF Name: Ph4nt0m 1ntrud3r (Easy)

### Description:
A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag. To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!

### Hint:
1. Filter your packets to narrow down your search.
2. Attacks were done in timely manner.
3. Time is essential

### Analysis:
Inside the PCAP, several TCP packets carry Base64-encoded data, but they are out of order time-wise. By filtering packets of specific lengths, extracting TCP payloads, sorting by timestamp, decoding Base64, and concatenating the output in correct order, we can reconstruct the full flag.

### Solution:
1. **Download file PCAP:**
	
	![f](./documentation/Screenshot%202025-06-23%20131540.png)

2. **Filter & extract payloads:**

	Use tshark to extract TCP payloads from TPC packets of desired lengths:

	![f](./documentation/Screenshot%202025-06-23%20131230.png)
	
3.  **Sort & decode:**

	![f](./documentation/Screenshot%202025-06-23%20131244.png )

### Flag:
**picoCTF{1t_w4snt_th4t_34sy_tbh_4r_959f50d3}**
