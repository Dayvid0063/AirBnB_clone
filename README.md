# AirBnB_clone

The goal of the project is to deploy on our server a simple copy of the AirBnB website.

We are not implementing all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, we will have a complete web application composed by:

A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
A website (the front-end) that shows the final product to everybody: static and dynamic.
A database or files that store data (data = objects)
An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Features

- command interpreter:

  - What is it: A command line interpreter is any program that allows the entering of commands and then executes those commands to the operating system. It's literally an interpreter of commands.

  - How to start it: To start a command interpreter, you can open the terminal or command prompt on your computer.

  - How to use it: The process of using a command interpreter involves typing commands into the terminal or command prompt and pressing the enter key to execute the command. The command interpreter then processes the command and returns the output to the user.

  - Examples:
    - To list all files in the current directory, type ls on a Unix-based system or dir on a Windows-based system.
    - To change the current directory, type cd followed by the name of the directory you want to change to.
    - To create a new directory, type mkdir followed by the name of the directory you want to create

- Website
- Database
- Api

## Lessons Learned

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is \*args and how to use it
- What is \*\*kwargs and how to use it
- How to handle named arguments in a function

## Documentation

[Python Packages](https://intranet.alxswe.com/concepts/66)
[Concept Page](https://intranet.alxswe.com/concepts/74)

## Usage/Examples

**Execution**

The shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Final Product

![Final Product 1](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240108T105001Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=98d7d0d5c074e0b85d07970b222095f249438a4ad4c3a58d3f5111148419dec3)

![Final Product 2](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/da2584da58f1d99a72f0a4d8d22c1e485468f941.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240108T105001Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cd6e7eb3efa0305b6eefb04c262b983d9bd6ac570bed1aa06572673d80f7ee8e)

## Authors

- [@cruso003](https://www.github.com/cruso003)
- [@Dayvid0063](https://github.com/Dayvid0063)
