#!/usr/bin/python3
"""
contains the console
"""
import cmd
import models
import re
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
classnames = {
    "BaseModel": BaseModel,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "User": User,
    "Review": Review,
    "State": State
    }


def parse_arg(arg):
    """parses and separates args"""
    return arg.split(" ")


def rem_chars(my_list):
    """removes the \" or \' character"""
    for i in range(len(my_list)):
        if my_list[i][0] == '"' or my_list[i][0] == "'":
            my_list[i] = my_list[i][1:-1]
    return my_list


class HBNBCommand(cmd.Cmd):
    """A class that contains the entry point of the command interpreter"""
    prompt = '(hbnb) '

    def default(self, string):
        """
        If your class does not include a specific command
        processor for a command, the method default()
        is called with the entire input line as an argument.
        """
        commands = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'count': self.do_count
        }

        # pattern = r'(\w+)\.(\w+)\(("?[\w-]*"?\)?,? ?)+({.*})?'
        if re.search(r'\.', string) is None:
            print("*** Unknown syntax: {}".format(string))
            return

        pattern = r'\w+(?=\.)'
        model = re.findall(pattern, string)
        pattern2 = r'(?<=\.)\w+'
        cmd = re.findall(pattern2, string)
        if model[0] not in classnames or cmd[0] not in commands:
            return

        dict_values = re.findall('{.*}', string)
        if dict_values:
            again = re.sub(dict_values[0], "", string)
            search = re.findall('[^()]+', again)
            search = re.findall('[^, ]+', search[1])
            new = re.split(': |, ', dict_values[0][1:-1])

            new = rem_chars(new)
            search = rem_chars(search)

            co_join = model + search
            co_join = co_join + new
            arg = " ".join(co_join)
            commands[cmd[0]](arg)
        else:
            search = re.findall('[^()]+', string)
            if len(search) > 1:
                search = search[1].split(', ')
                search = rem_chars(search)
                co_join = model + search
                arg = " ".join(co_join)
                commands[cmd[0]](arg)
            else:
                commands[cmd[0]](" ".join(model))

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
        """destroys an object from the json database"""
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

    def do_count(self, arg):
        """counts the number of intsnaces of
        an object"""
        arg_list = parse_arg(arg)
        all_objs = storage.all()
        result = []
        for key, value in all_objs.items():
            classname, id = key.split(".")
            if arg_list[0] == classname:
                result.append(all_objs[key].__str__())
        print(len(result))

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
        argl = parse_arg(arg)
        all_objs = storage.all()
        if argl[0]:
            if argl[0] not in classnames:
                print("** class doesn't exist **")
            elif len(argl) == 1:
                print("** instance id missing **")
            elif f"{argl[0]}.{argl[1]}" not in all_objs:
                print("** no instance found **")
            elif len(argl) == 2:
                print("** attribute name missing **")
            elif len(argl) == 3:
                print("** value missing **")
            else:
                obj = all_objs[f"{argl[0]}.{argl[1]}"]
                for i in range(2, len(argl), 2):
                    if argl[i + 1][0] == '"' and argl[i + 1][-1] == '"':
                        argl[i + 1] = argl[i + 1][1:-1]
                    if argl[i] in obj.to_dict():
                        val_type = type(getattr(obj, argl[i]))
                        setattr(obj, argl[i], val_type(argl[i + 1]))
                    else:
                        setattr(obj, argl[i], argl[i + 1])
                storage.save()
        else:
            print("** class name missing ** ")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
