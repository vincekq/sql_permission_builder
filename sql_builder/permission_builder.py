import csv
from helper import file_ops


class MYSQLQueryBuilder:
    host = "%"

    def __init__(self, user, password, schema, privilege_file):
        self.user = user
        self.password = password
        self.schema = schema
        self.privilege_file = privilege_file

    def validator(self):
        file_ops.validator(self.privilege_file)

    def extract_content(self):
        self.validator()
        try:
            with open(self.privilege_file) as db_permissions:
                reader = csv.reader(db_permissions, delimiter=",", quotechar='"')
                data_read = [row for row in reader]
                headers = data_read[0]
                data = data_read[1:]
            return headers, data
        except Exception as err:
            print(err)
            exit()

    @staticmethod
    def decode_password(password):
        masked_password = password[-3:].rjust(len(password), "*")
        return masked_password

    @property
    def user_query(self):
        query = f"CREATE USER '{self.user}'@'{self.host}' IDENTIFIED BY '{self.password}'; \n\n"
        masked = self.decode_password(self.password)
        print(f"CREATE USER '{self.user}'@'{self.host}' IDENTIFIED BY '{masked}';")
        print(f"""
                {'-' * 40}
                """)
        return query

    @property
    def privileges_query(self):
        _, data = self.extract_content()
        tray = []
        for row in data:
            table = row[0]
            privilege = (row[1]).upper()
            query = f"GRANT {privilege} ON `{self.schema}`.`{table}` TO '{self.user}'@'{self.host}';"
            print(query)
            tray.append(query)
        return tray

    def write_privileges_to_file(self, filename) -> object:
        """

        :rtype: object
        """
        user_query = self.user_query
        data = self.privileges_query
        with open(filename, mode='wt', encoding='utf-8') as my_file:
            my_file.write(user_query)
            my_file.write('\n'.join(data))
        my_file.close()
        return user_query, data
    