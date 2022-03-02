import os
import json


class JSONDataBase:

    def __init__(self, folder_name, file_name):
        self.__folder = folder_name
        self.__file = file_name
        self.__file_loc = None
        self.__connection = None

    def setup(self):
        os.makedirs(self.__folder, exist_ok=True)
        self.__file_loc = os.path.join(self.__folder, self.__file)

    def insert_values(self, features, values):
        if not os.path.isfile(self.__file_loc):
            data = []
        else:
            self.__connection = open(self.__file_loc)
            data = json.load(self.__connection)
            self.close()

        info = {}
        for (feature, value) in zip(features, values):
            if value != "?":
                info[feature] = value
        data.append(info)
        self.__connection = open(self.__file_loc, 'w')
        json.dump(data, self.__connection, indent=4)
        self.close()

    def close(self):
        self.__connection.close()


