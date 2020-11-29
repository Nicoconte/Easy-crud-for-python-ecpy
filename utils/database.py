import mysql.connector


class Database:
    host = ""
    __database = ""
    __user = ""
    __password = ""
    
    __connection = None

    def __init__(self, host, db, user, password):
        self.__host = host
        self.__database = db
        self.__user = user
        self.__password = password

    
    def setConnection(self):
        self.__connection = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__database
        )

        return self.__connection
