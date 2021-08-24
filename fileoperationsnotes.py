'''File Operations:-
----------------

Python comes with a default mechanisam to perform some file opertions on  file.
* The basic functions that can perform	on a file are:-
1. open	
2. read ---> "r"
3. write --> "w"
4. append --> "a"
5. close

-- Open method takes atleast one parameter,atmost two parameter i.e.., 1st represents file name and file path and 2nd is operation mode.
-- O/P format is always a file pointer object.

Syntax:-
-------

variable_name = open(r"Filepath/Filename","operation mode = "r"")

Example:-
--------

fp = open(r"C:\Users\Venkatesh\OneDrive\Desktop\venky.txt")
print(fp)
print(dir(fp))





























fp = open(r"C:\Users\Venkatesh\OneDrive\Desktop\venky.txt")
print(fp)
print(dir(fp))
