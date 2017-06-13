from enum import Enum

import _mysql
from MySQLdb.constants import FIELD_TYPE


class UserStatus(Enum):
    Active = 1
    Inactive = 2

    def __str__(self):
        return self.name


class DBConnector:
    def __init__(self):
        field_converter = {FIELD_TYPE.LONG: int,
                           FIELD_TYPE.STRING: self.__string_convert,
                           FIELD_TYPE.VAR_STRING: self.__var_string_convert}
        self.__connection = _mysql.connect(db="Users", conv=field_converter, user='mysql', passwd='ws3d1xc')
        self.__cash = {}

    def get_courses(self):
        if "courses" not in self.__cash:
            self.__connection.query("CALL getCourses ()")
            self.__cash["courses"] = self.__connection.store_result().fetch_row(maxrows=0, how=1)
        return self.__cash.get("courses", [])

    def get_users(self, name=""):
        if "users" not in self.__cash:
            self.__connection.query("CALL getListeners ()")
            self.__cash["users"] = self.__connection.store_result().fetch_row(maxrows=0, how=1)
        if name:
            filtered_users = []
            for user in self.__cash.get("users", []):
                if name.lower() in user["name"].lower():
                    filtered_users.append(user)
            return filtered_users
        return self.__cash.get("users", [])

    def __string_convert(self, var):
        if var.decode() == "Inactive":
            return UserStatus.Inactive
        else:
            return UserStatus.Active

    def __var_string_convert(self, var):
        return var.decode()
