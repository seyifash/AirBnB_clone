#!/usr/bin/python3
"""
contains the console
"""
import cmd
import models
from datetime import datetime
from models import storage
from models.base_model import BaseModel
classnames = {"BaseModel": BaseModel}

def parse_arg(arg):
    """parses and separates args"""
    return arg.split(" ")


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

    def do_create(self, arg):
        """creates the instance of the variable"""
        if arg:
            if arg not in classnames:
                print("** class doesn't exist **")
            else:
                print(eval(arg)().id)
                storage.save()
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """shows the object based on id"""
        arg_list = parse_arg(arg)
        all_objs = storage.all()
        if arg_list[0]:
            if arg_list[0] not in classnames:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            elif f"{arg_list[0]}.{arg_list[1]}" not in all_objs:
                print("** no instance found **")
            else:
                print(all_objs[f"{arg_list[0]}.{arg_list[1]}"])
        else:
            print("** class name missing ** ")

    def do_destroy(self, arg):
        """destroys an onject from the json database"""
        arg_list = parse_arg(arg)
        all_objs = storage.all()
        if arg_list[0]:
            if arg_list[0] not in classnames:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            elif f"{arg_list[0]}.{arg_list[1]}" not in all_objs:
                print("** no instance found **")
            else:
                del all_objs[f"{arg_list[0]}.{arg_list[1]}"]
                storage.save()
        else:
            print("** class name missing ** ")

    def do_all(self, arg):
        """prints all the objs based on or not on a class"""
        arg_list = parse_arg(arg)
        all_objs = storage.all()
        result = []
        if arg_list[0]:
            if arg_list[0] not in classnames:
                print("** class doesn't exist **")
            else:
                for key, value in all_objs.items():
                    classname, id = key.split(".")
                    if arg_list[0] == classname:
                        result.append(all_objs[key].__str__())
                print(result)
        else:
            for obj_id in all_objs.keys():
                result.append(all_objs[obj_id].__str__())
            print(result)

    def do_update(self, arg):
        """updates an attribute in an object"""
        arg_list = parse_arg(arg)
        all_objs = storage.all()
        if arg_list[0]:
            if arg_list[0] not in classnames:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            elif f"{arg_list[0]}.{arg_list[1]}" not in all_objs:
                print("** no instance found **")
            elif len(arg_list) == 2:
                print("** attribute name missing **")
            elif len(arg_list) == 3:
                print("** value missing **")
            else:
                obj = all_objs[f"{arg_list[0]}.{arg_list[1]}"]
                if arg_list[3][0] == '"' and arg_list[3][-1] == '"':
                    arg_list[3] = arg_list[3][1:-1]
                if arg_list[2] in obj.to_dict():
                    val_type = type(getattr(obj, arg_list[2]))
                    setattr(obj, arg_list[2], val_type(arg_list[3]))
                else:
                    setattr(obj, arg_list[2], arg_list[3])
                storage.save()
        else:
            print("** class name missing ** ")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
