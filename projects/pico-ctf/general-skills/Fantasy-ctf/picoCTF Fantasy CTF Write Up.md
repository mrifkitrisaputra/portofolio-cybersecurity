##  CTF Name: Fantasy CTF (Easy)

### Description:
Play this short game to get familiar with terminal applications and some of the most important rules in scope for picoCTF.

### Hint:
When a choice is presented like [a/b/c], choose one, for example: `c` and then press Enter.

### Analysis:
This challenge serves as an interactive introduction for newcomers to CTFs. Players are asked to connect to a remote server via netcat and go through a series of text-based prompts. The game presents multiple-choice questions (such as A, B, or C), and users are expected to select the correct options based on context — for example, choosing "C" to register a private account. Once the flow is completed correctly, the server will reveal the flag as a reward.

### Solution:
1. **Connect to the server:**
	
	![f](./documentation/Screenshot%202025-06-23%20113813.png)
	
3. **Interact with the simulation:**
	Once connected, you will be prompted with a series of choices like:
	
	![f](./documentation/Screenshot%202025-06-23%20113845.png)

	![f](./documentation/Screenshot%202025-06-23%20114004.png)
	
4. **Retrieve the flag:**
	At the end of the interaction, the terminal will display the flag. Copy and save it.
	
	![f](./documentation/Screenshot%202025-06-23%20114042.png)

### Flag:
**picoCTF{m1113n1um_3d1710n_da2cd4b9}**
