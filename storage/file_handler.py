import json
import os

class FileHandler:
    def __init__(self,filepath:str):
        self.filepath = filepath

    def read_data(self):
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath,"r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def write_data(self,data):
        with open(self.filepath,"w") as file:
            json.dump(data,file,indent=4)
