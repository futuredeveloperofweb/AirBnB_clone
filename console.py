#!/usr/bin/python3
""" A modeul that has a program called console.py that contains
the entry point of the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from models.user import User
import re


class HBNBCommand(cmd.Cmd):
    """A command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print()
        return True

    def emptyline(self):
        '''An empty line + ENTER shouldn’t execute anything'''
        pass

    def default(self, arg):
        '''a function that convert some input methods into default methods'''
        cmd = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        d = re.search(r"\.", arg)
        if d is not None:
            lst = [arg[:d.span()[0]], arg[d.span()[1]:]]
            d = re.search(r"\((.*?)\)", lst[1])
            if d is not None:
                part = [lst[1][:d.span()[0]], d.group()[1:-1]]
                if part[0] in cmd.keys():
                    c = f'{lst[0]} {part[1]}'
                    return cmd[part[0]](c)
        print(f'*** Unknown syntax: {arg} ***')
        return False

    def do_create(self, arg):
        '''Creates a new instance of BaseModel'''
        args = arg.split()

        if not args:
            print('** class name missing **')
        elif args[0] not in globals():
            print('** class doesn\'t exist **')
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        '''Prints the string representation of an instance based
        on the class name and id
        '''
        args = arg.split()

        if not args:
            print('** class name missing **')
        elif args[0] not in globals():
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in storage.all():
            print('** no instance found **')
        else:
            print(storage.all()[f'{args[0]}.{args[1]}'])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        obj_dict = models.storage.all()

        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f'{args[0]}.{args[1]}' not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f'{args[0]}.{args[1]}']
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name.
        """
        args = arg.split()

        if not args:
            print([str(o) for o in storage.all().values()])
        elif args[0] not in globals():
            print("** class doesn't exist **")
        else:
            instances = [
                str(o) for k, o in storage.all().items() if args[0] in k]
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f'{args[0]}.{args[1]}' not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print('** value missing **')
        else:
            k = f'{args[0]}.{args[1]}'
            ob = storage.all()[k]
            attr = args[2]
            val = args[3]
            setattr(ob, attr, type(val)(val))
        storage.save()

    def do_count(self, arg):
        '''retrieve the number of instances of a class:
        <class name>.count()
        '''
        args = arg.split()
        c = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == args[0]:
                c = c + 1
        print(c)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
