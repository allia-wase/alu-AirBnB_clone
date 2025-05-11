import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Handles serialization and deserialization of BaseModel instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, val in objs.items():
                    self.__objects[key] = BaseModel(**val)

