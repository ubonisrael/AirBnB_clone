#!/usr/bin/python3
"""Contains the HBNB class"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review
                   }
        return classes

    def do_quit(self, args):
        """quits the console
        """
        return True
    
    def do_EOF(self, args):
        """handles the EOF character
        """
        print()
        return True
    
    def emptyline(self):
        """Empty line, nothing happens
        """
        pass

    def do_create(self, args):
        """Creates a new instance of a model, saves it
        (to the JSON file) and prints the id
        """
        args_list = args.split()
        if len(args_list) == 0:
            print('** class name missing **')
            return
        try:
            my_obj_class = self.classes()[args_list[0]]
            cls_instance = my_obj_class()
            storage.save()
            print(cls_instance.id)
        except KeyError as e:
            print('** class doesn\'t exist **')
            return

    def do_show(self, args):
        """ Prints the string representation of an instance
        based on the class name and id
        """
        args_list = args.split()
        if len(args_list) == 0:
            print('** class name missing **')
            return
        if len(args_list) < 2:
            print('** instance id missing **')
            return
        try:
            self.classes()[args_list[0]]
            obj_dict = storage.all()
            for k, v in obj_dict.items():
                my_id = k.split('.')
                if my_id[0] == args_list[0] and my_id[1] == args_list[1]:
                    print(v)
                    return
            print('** no instance found **')
        except KeyError as e:
            print('** class doesn\'t exist **')
            return

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args_list = args.split()
        if len(args_list) == 0:
            print('** class name missing **')
            return
        if len(args_list) < 2:
            print('** instance id missing **')
            return
        try:
            self.classes()[args_list[0]]
            obj_dict = storage.all()
            for k in obj_dict.keys():
                my_id = k.split('.')
                if args_list[0] == my_id[0] and args_list[1] == my_id[1]:
                    del obj_dict[k]
                    storage.save()
                    return
            print('** no instance found **')
        except KeyError as e:
            print('** class doesn\'t exist **')
            return

    def do_all(self, args):
        """ Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        args_list = args.split()
        obj_dict = storage.all()
        if len(args_list) == 0:
            len_obj_dict = len(obj_dict)
            if len_obj_dict > 0:
                print("[", end="")
                index = 0
                for v in obj_dict.values():
                    if index + 1 < len_obj_dict:
                        print("\"", v, sep="", end="\", ")
                    else:
                        print(v, end="\"")
                    index += 1
                print("]")
            return

        try:
            self.classes()[args_list[0]]
            obj_list = []
            for k, v in obj_dict.items():
                if k.split('.')[0] == args_list[0]:
                    obj_list.append(v)
            len_obj_list = len(obj_list)
            if len_obj_list > 0:
                print("[", end="")
                index = 0
                for v in obj_list:
                    if index + 1 < len_obj_list:
                        print("\"", v, sep="", end="\", ")
                    else:
                        print(v, end="\"")
                    index += 1
                print("]")
        except KeyError as e:
            print('** class doesn\'t exist **')
            return

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        args_list = args.split()
        args_len = len(args_list)
        if args_len == 0:
            print('** class name missing **')
            return
        if args_len < 2:
            print('** instance id missing **')
            return
        try:
            self.classes()[args_list[0]]
            obj_dict = storage.all()
            for k, v in obj_dict.items():
                my_id = k.split('.')
                if args_list[0] == my_id[0] and args_list[1] == my_id[1]:
                    if args_len < 3:
                        print('** attribute name missing **')
                        return
                    if args_len < 4:
                        print('** value missing **')
                        return
                    setattr(v, args_list[2], args_list[3])
                    return
            print('** no instance found **')
        except KeyError as e:
            print('** class doesn\'t exist **')
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
