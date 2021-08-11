import secrets
import string


class Credentials:

    acceptable_length = 16

    def __init__(self, filename):
        """dbuser_schema.csv is the acceptable file format"""

        self.filename = filename

    @property
    def db_user(self):
        db_user = self.filename.split("__")[0]
        if len(db_user) >= self.acceptable_length:
            print(f"invalid length for db_username {db_user}. Acceptable length is {self.acceptable_length}")
            exit()
        return db_user

    @property
    def db_schema(self):
        return self.filename.split("__")[1].split(".")[0]

    @staticmethod
    def db_password(password_length=12):
        special_characters = '!@<>+_&'
        password = ''.join(
            (secrets.choice(string.ascii_letters + string.digits + special_characters) for _ in range(password_length)))
        return password
