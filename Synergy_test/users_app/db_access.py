import MySQLdb
from MySQLdb.cursors import DictCursor

COURSES = {"cash_key": "courses", "procedure": "getCourses"}
USERS = {"cash_key": "users", "procedure": "getListeners"}
CACHE = {}


class DBConnector:
    def __init__(self):
        self.__connection = MySQLdb.connect(db="Users")

    def __del__(self):
        self.__connection.close()

    def get_courses(self):
        self.__verify_cash(COURSES)
        return CACHE.get("courses", [])

    def get_user_by_id(self, user_id):
        try:
            user_id = int(user_id)
            coursor = self.__connection.cursor(DictCursor)
            coursor.callproc(procname="getListenerDetail", args=(user_id,))
            user_detail = coursor.fetchone()
            coursor.close()
            user_detail["courses"] = self.__parse_courses(user_detail.get("courses"))
        except Exception as e:
            print("### ERROR: ", e)
            return {}
        return user_detail

    def __parse_courses(self, courses):
        if not courses:
            return
        parsed_courses = {}
        for course in courses.split(';'):
            course_id = int(course.split(',')[0])
            course_name = course.split(',')[1]
            parsed_courses[course_id] = course_name
        return parsed_courses

    def get_users(self, name=""):
        self.__verify_cash(USERS)
        if name:
            filtered_users = []
            for user in CACHE.get("users", []):
                if name.lower() in user["name"].lower():
                    filtered_users.append(user)
            return filtered_users
        return CACHE.get("users", [])

    def add_new_user(self, user):
        try:
            coursor = self.__connection.cursor()
            coursor.callproc(procname="addListener", args=(user["name"],
                                                           user["mail"],
                                                           user["phone"] or None,
                                                           user["mobile"] or None,
                                                           user["status"]))
            self.__connection.commit()
            coursor.close()
            CACHE.pop("users", None)
        except Exception as e:
            print("### ERROR: ", e)

    def update_user(self, user):
        try:
            coursor = self.__connection.cursor()
            coursor.callproc(procname="editListener", args=(user["id"],
                                                            user["mail"] or None,
                                                            user["phone"] or None,
                                                            user["mobile"] or None,
                                                            user["status"]))
            self.__connection.commit()
            coursor.close()
            CACHE.pop("users", None)
        except Exception as e:
            print("### ERROR: ", e)

    def add_course_to_user(self, user, course):
        try:
            coursor = self.__connection.cursor()
            coursor.callproc(procname="addListenerCourse", args=(user, course))
            self.__connection.commit()
            coursor.close()
        except Exception as e:
            print("### ERROR: ", e)

    def remove_course_from_user(self, user, course):
        try:
            coursor = self.__connection.cursor()
            coursor.callproc(procname="removeListenerCourse", args=(user, course))
            self.__connection.commit()
            coursor.close()
        except Exception as e:
            print("### ERROR: ", e)

    def remove_user(self, user_id):
        try:
            coursor = self.__connection.cursor()
            coursor.callproc(procname="removeListener", args=(user_id,))
            self.__connection.commit()
            coursor.close()
            CACHE.pop("users", None)
        except Exception as e:
            print("### ERROR: ", e)

    def __verify_cash(self, params):
        if params["cash_key"] not in CACHE:
            try:
                coursor = self.__connection.cursor(DictCursor)
                coursor.callproc(procname=params["procedure"])
                CACHE[params["cash_key"]] = coursor.fetchall()
                coursor.close()
            except Exception as e:
                print("### ERROR: ", e)
