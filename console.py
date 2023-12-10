#!/usr/bin/python3
""" A modeul that has a program called console.py that contains
the entry point of the command interpreter
"""
import models
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    a_match = re.search(r"\{(.*?)\}", arg)
    b_match = re.search(r"\[(.*?)\]", arg)

    if a_match is None:
        if b_match is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:b_match.span()[0]])
            ret_list = [i.strip(",") for i in lexer]
            ret_list.append(b_match.group())
            return ret_list
    else:
        lexer = split(arg[:a_match.span()[0]])
        ret_list = [i.strip(",") for i in lexer]
        ret_list.append(a_match.group())
        return ret_list


class HBNBCommand(cmd.Cmd):
    """A command interpreter class"""

    prompt = "(hbnb) "
    allowed_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

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
        """Default behavior for cmd module when input is invalid"""
        command_dict = {
           "all": self.do_all,
           "show": self.do_show,
           "destroy": self.do_destroy,
           "count": self.do_count,
           "update": self.do_update
        }
        dot_match = re.search(r"\.", arg)
        if dot_match is not None:
            a_list = [arg[:dot_match.span()[0]], arg[dot_match.span()[1]:]]
            paren_match = re.search(r"\((.*?)\)", a_list[1])
        if paren_match is not None:
            c = [a_list[1][:paren_match.span()[0]], paren_match.group()[1:-1]]
            if c[0] in command_dict.keys():
                call = "{} {}".format(a_list[0], c[1])
                return command_dict[c[0]](call)
        print("*** Unknown syntax: {}".format(arg))
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
            storage.all().save()

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        arglist = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arglist[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
