##  CTF Name: EVEN RSA CAN BE BROKEN??? (Easy)

### Description:
This service provides you an encrypted flag. Can you decrypt it with just N & e?

### Hint:
1. How much do we trust randomness?
2. Notice anything interesting about N?
3. Try comparing N across multiple requests

### Analysis:
Ordinarily, RSA moduli `N = p * q` should be **odd**, since `p` and `q` are large odd primes. However, every `N` you receive is observed to be **even**, implying one of the primes is `2` or the primes are **reused across key generations.**  This strongly indicates a **non-coprime moduli vulnerability**—two moduli sharing a common prime factor. Compute their `gcd` to find that factor and then factor both moduli.

### Solution:
1. **Connect via netcat:**

	![f](./documentation/Screenshot%202025-06-25%20181542.png)

2. **Calculate RSA using decode online like [RSA Cipher](https://www.dcode.fr/rsa-cipher):**

	input the values we get from netcat into the fields for _C_, _e_, and _N_ and click **Calculate / Decrypt**
	
	![f](./documentation/Screenshot%20(735).png)

### Flag:
**picoCTF{tw0_1$_pr!m3f81fef0a}**
