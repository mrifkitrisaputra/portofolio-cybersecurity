##  CTF Name: DISKO 1 (easy)

### Description:
Can you find the flag in this disk image?
### Hint:
1. Maybe Strings could help? If only there was a way to do that?

### Analysis:
In this challenge, we are provided with a raw disk image file: `disko-1.dd`.  
Our goal is to extract a hidden flag from within the image. Let’s walk through a straightforward method to accomplish this using the **`strings`** utility.

### Solution:
**1. **Extract the disk file****  
The given file is compressed with gzip. First, we extract it using:
![f](./documentation/Screenshot%202025-06-23%20091326.png)

**2. Identify the file type**
Next, we use the `file` command to determine the image’s format:

![f](./documentation/Screenshot%202025-06-23%20091334.png)
The output reveals that the image contains a **FAT32 filesystem**, commonly used in USB drives. It appears to be a raw filesystem dump without a partition table.

**3. Search for the flag**
We then use `strings` in combination with `grep` to search for any string containing "picoCTF":

![f](./documentation/Screenshot%202025-06-23%20091344.png)

### Flag:
**picoCTF{1t5_ju5t_4_5tr1n9_e3408eef}**
