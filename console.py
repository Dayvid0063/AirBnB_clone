#!/usr/bin/python3
"""
This module defines a simple command-line interpreter for HBNB.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class defines the command-line interpreter for HBNB.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
