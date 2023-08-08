#!/usr/bin/python3
"""
contains the console
"""
import cmd
import models
from datetime import datetime
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """A class that contains the entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ctrl+D to exit the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """an emptyline + Enter doesnt execute anything"""
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
