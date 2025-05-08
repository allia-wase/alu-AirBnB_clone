import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print()
        return True

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        if arg == "BaseModel":
            obj = BaseModel()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"BaseModel.{args[1]}"
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"BaseModel.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        objects = storage.all()
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        args = arg.split()
        if len(args) < 4:
            print("** usage: update <class name> <id> <attribute name> <value> **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        setattr(obj, args[2], eval(args[3]))
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
