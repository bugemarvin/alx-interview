<div align=center>
<h1>Pascal's Triangle</h1>
</div>

## Introduction

Pascal's triangle is a triangular array of numbers in which the first and last number in each row is 1, and each of the other numbers is the sum of the two numbers directly above it.

## Question

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:
* Returns an empty list if `n <= 0`
* You can assume `n` will be always an integer

## Sample Code
To achive below code output please use below sample
```
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 
```

## My Output
<img src="https://github.com/bugemarvin/alx-interview/blob/master/0x00-pascal_triangle/image.png"/>
