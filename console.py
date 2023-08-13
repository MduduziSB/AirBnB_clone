#!/usr/bin/python3
"""Contains the entry point of the HBNB command interpreter"""

import cmd
import sys
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """A custom command interpreter class"""

    prompt = "(hbnb) "
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review
            }

    def do_create(self, line):
        """Creates a new instance of a class"""
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return False

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False

        new_instance = HBNBCommand.classes["BaseModel"]()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return False

        class_name = args[0]
        if class_name not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        id = args[1]
        key = f"{class_name}.{id}"
        if key in storage.all():
            obj = storage.all()[key]
            print(obj)
        else:
            print("** no instance found **")
            return False

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(line)

        if len(args) < 1:
            print("** class name missing **")
            return False
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        id = args[1]
        key = f"{class_name}.{id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")
            return False

    def do_all(self, line):
        """ Prints all string representation of all instances."""
        args = shlex.split(line)
        instances = []
        if args and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if not args or args[0] == value.__class__.__name__:
                instances.append(str(value))
        print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = shlex.split(line)

        if len(args) < 1:
            print("** class name missing **")
            return False

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        id = args[1]
        key = f"{class_name}.{id}"
        if key not in storage.all():
            print("** no instance found **")
            return False

        if len(args) < 3:
            print("** attribute name missing **")
            return False

        if len(args) < 4:
            print("** value missing **")
            return False

        attribute_name = args[2]
        attribute_value = args[3]

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def emptyline(self):
        """prevents previous command from running on passing
        empty line to the interpreter"""
        pass

    def do_quit(self, line):
        """quits the interpreter"""
        print("")
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """Returns true on successful execution"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
