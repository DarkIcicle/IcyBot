import pymysql


class MySQLConnection:
    def __init__(self):
        self.user = 'root'
        self.password = ''
        self.host = 'localhost'
        self.port = 3306
        self.db = 'discorddb'
        self.cursor_class = pymysql.cursors.DictCursor
        self.autoCommit = True
        self.connection = None

    def connect(self):
        try:
            print("Attempting to connect to database...")
            self.connection = pymysql.connect(user=self.user, password=self.password, host=self.host, port=self.port,
                                              db=self.db, cursorclass=self.cursor_class, autocommit=self.autoCommit)
        except pymysql.Error as err:
            print(err)

    def user_exists(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                statement = "SELECT * FROM `user_data` WHERE `USERID`=%s"
                cursor.execute(statement, user_id)
                result = cursor.fetchone()
                if result is not None:
                    return True
                return False
        except cursor.Error as err:
            print(err)

    def get_experience(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                statement = "SELECT * FROM `user_data` WHERE `USERID`=%s"
                cursor.execute(statement, user_id)
                result = cursor.fetchone()['EXPERIENCE']
                return result
        except cursor.Error as err:
            print(err)

    def get_level(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                statement = "SELECT * FROM `user_data` WHERE `USERID`=%s"
                cursor.execute(statement, user_id)
                result = cursor.fetchone()['LEVEL']
                return result
        except cursor.Error as err:
            print(err)

    def update_experience(self, user_id, amount: int):
        try:
            with self.connection.cursor() as cursor:
                statement = "UPDATE `user_data` SET EXPERIENCE=%s WHERE `USERID`=%s"
                cursor.execute(statement, (self.get_experience(user_id) + amount, user_id))
        except cursor.Error as err:
            print(err)

    def set_experience(self, user_id, amount: int):
        try:
            with self.connection.cursor() as cursor:
                statement = "UPDATE `user_data` SET EXPERIENCE=%s WHERE `USERID`=%s"
                cursor.execute(statement, (amount, user_id))
        except cursor.Error as err:
            print(err)

    def update_level(self,user_id):
        try:
            with self.connection.cursor() as cursor:
                statement = "UPDATE `user_data` SET LEVEL=%s WHERE `USERID`=%s"
                cursor.execute(statement, (self.get_level(user_id) + 1, user_id))
        except cursor.Error as err:
            print(err)

    def get_coins(self, user_id):
        try:
            with self.connection.cursor() as cursor:
                statement = "SELECT * FROM `user_data` WHERE `USERID`=%s"
                cursor.execute(statement, user_id)
                result = cursor.fetchone()['COINS']
                return result
        except cursor.Error as err:
            print(err)

    def update_coins(self,user_id):
        try:
            with self.connection.cursor() as cursor:
                statement = "UPDATE `user_data` SET COINS=%s WHERE `USERID`=%s"
                cursor.execute(statement, (self.get_level(user_id) + 1, user_id))
        except cursor.Error as err:
            print(err)

    def create_user(self, user_id, name):
        if not self.user_exists(user_id):
            try:
                with self.connection.cursor() as cursor:
                    statement = "INSERT INTO `user_data` (`USERID`,`NAME`,`COINS`,`EXPERIENCE`, `LEVEL`) VALUE (%s,%s,%s,%s,%s)"
                    cursor.execute(statement, (user_id, name, 0, 0, 1))
            except cursor.Error as err:
                print(err)