from sql_builder import mysqluser
from sql_builder import permission_builder as pb
from helper import run_mode as run_mode

if __name__ == "__main__":
    file_location, output_file_path = run_mode.runner()
    run_mode.csv_standard()
    filename = input("Kindly input the name of the file: ")

    user = mysqluser.Credentials(filename)
    username, schema, password = user.db_user, user.db_schema, user.db_password(password_length=12)
    abs_filename = file_location + str(filename)
    query_file = output_file_path + str(filename.split(".")[0]) + ".sql"
    permissions = pb.MYSQLQueryBuilder(username, password, schema, abs_filename)
    if permissions.write_privileges_to_file(query_file):
        run_mode.success(output_file_path)
    else:
        run_mode.failure()
