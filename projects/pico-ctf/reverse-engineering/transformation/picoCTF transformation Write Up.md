##  CTF Name: transformation (Easy)

### Description:
I wonder what this really is... [enc](https://mercury.picoctf.net/static/a757282979af14ab5ed74f0ed5e2ca95/enc)

  `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

### Hint:
You may find some decoders online

### Analysis:
Inspecting the challenge description hints at a transformation applied via:
``''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in ...
``

This indicates that every pair of ASCII characters was combined into a single 16‑bit code, producing characters in the 0xXXXX range

### Solution:
1. **Download & cat file challenge**

	![f](./documentation/Screenshot%202025-06-25%20174400.png)

2. **Decode using magic tools [CyberChef](https://gchq.github.io/CyberChef/):**

	![f](./documentation/Screenshot%20(734).png)

### Flag:
**picoCTF{16_bits_inst34d_of_8_d52c6b93}**
