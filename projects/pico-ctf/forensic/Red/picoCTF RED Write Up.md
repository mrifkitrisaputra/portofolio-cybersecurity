##  CTF Name: RED (Easy)

### Description:
RED, RED, RED, RED

### Hint:
1. The picture seems pure, but is it though?
2. Red?Ged?Bed?Aed?
3. Check whatever Facebook is called now.

### Analysis:
PNG images can hide data using steganographic techniques. By running `zsteg -a red.png`, we can extract hidden data embedded in the image’s LSB (Least Significant Bit). The output includes a Base64-encoded string. Decoding that string reveals the flag.

### Solution:
1. ****Download the `red.png`** file from the challenge:**

	![f](./documentation/Screenshot%202025-06-23%20122132.png)

2. **Install Zsteg and run ``zsteg -a red.png``**

	![f](./documentation/Screenshot%202025-06-23%20122646.png)

	You should find a string we need

3. ****Decode the Base64** string using a tool like [CyberChef](https://gchq.github.io/CyberChef/)**

	![f](./documentation/Screenshot%20(720).png)

### Flag:
**picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}**
