# N Queens

## Requirements
### General
Allowed editors: vi, vim, emacs\
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)\
All your files should end with a new line\
The first line of all your files should be exactly `#!/usr/bin/python3`\
A README.md file, at the root of the folder of the project, is mandatory\
Your code should use the PEP 8 style (version 1.7.*)\
All your files must be executable\
<img src="https://github.com/bugemarvin/alx-interview/blob/master/0x05-nqueens/judth_polgar.jpg" />\
Chess grandmaster Judit Polgár, the strongest female chess player of all time
# Task
Usage: `nqueens N`\
If the user called the program with the wrong number of arguments, `print Usage: nqueens N`, followed by a new line, and `exit` with the status `1`\
where `N` <b>must be an integer</b> `greater` or `equal` to `4`\
If `N` <b>is not an integer</b>, `print N must be a number`, followed by a `new line`, and `exit` with the `status 1`\
If `N is smaller than 4`, `print N must be at least 4`, followed by a `new line`, and `exit` with the `status 1`\
The program should print every possible solution to the problem\
One solution per line
## Format: see example

```
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$
```

