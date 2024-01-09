#!/usr/bin/python3
"""Contains the HBNB class"""
import cmd
from models import storage, base_model

class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self):
        """quits the console"""
        return True
    
    def do_create(self, cls_name):
        """Creates a new instance of a model, saves it (to the JSON file) and prints the id"""
        cls_instance = base_model.BaseModel()
        print(storage.all)
        storage.save()
        print(cls_instance.id)

    def do_create(self, cls_name, instance_id):
        """ Prints the string representation of an instance based on the class name and id"""
        print(storage.all)
        storage.save()

        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
