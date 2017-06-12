from enum import Enum

import _mysql
from MySQLdb.constants import FIELD_TYPE


class UserStatus(Enum):
    Active = 1
    Inactive = 2


def string_convert(var):
    if var.decode() == "Inactive":
        return UserStatus.Inactive
    else:
        return UserStatus.Active


def var_string_convert(var):
    return var.decode()

db_conv = {FIELD_TYPE.LONG: int,
           FIELD_TYPE.STRING: string_convert,
           FIELD_TYPE.VAR_STRING: var_string_convert}

db = _mysql.connect(user='mysql', passwd='ws3d1xc', db='Users', conv=db_conv)
db.query("CALL getListeners()")
res = db.store_result()
print(res.fetch_row(maxrows=0, how=1))



