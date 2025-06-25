##  CTF Name:  interencdec (Easy)

### Description:
Can you get the real meaning from this file.

### Hint:
Engaging in various decoding processes is of utmost importance

### Analysis:
This looks like a Base64 string. When decoded, it reveals another Base64 string, and finally a garbled text that appears to use Caesar cipher. This suggests a multi-layer decoding: **Base64 → Base64 → Caesar**.

### Solution:
1. **Download & cat file challange:**

	![f](./documentation/Screenshot%202025-06-25%20172034.png)

	This looks like a base64 string
	
2. **Decode using base64:**
	
	![f](./documentation/Screenshot%202025-06-25%20172053.png)

	this format looks like our flag but not base64 string

3. **Decode flag using [Caesar Chiper](https://www.dcode.fr/caesar-cipher):**

	![f](./documentation/Screenshot%20(733).png)
		
### Flag:
**picoCTF{caesar_d3cr9pt3d_ea60e00b}**
