from helper import color_grade as cg

run_mode, file_fmt, file_location, output_file_path = 'short', 'user__schema.csv', "/Users/vquianoo/Documents/DB_DOCS/privilege_document/", '/Users/vquianoo/Documents/DB_DOCS/privilege_queries/'


def runner():
    start_mode = f"""
        {'-' * 40}
        # Script by Vincent Quainoo
        # Run_mode: {run_mode}
        # File naming convention: {file_fmt}
        # file_location: {file_location}
        # file_output_location: {output_file_path}
        # test_file: bayport_ussd__bayport_ussd.csv
    
        {'-' * 40}
        """
    print(start_mode)
    return file_location, output_file_path


def csv_standard():
    MSG = cg.color.BOLD + "THE CSV FILE MUST BE IN THIS FORMAT" + cg.color.END
    start_mode = f"""
        {MSG}
        {'-' * 40}
         account_creation     | SELECT, INSERT
         account_cancellation | SELECT, INSERT, DELETE
         mandates             | UPDATE, INSERT
         logs                 | SELECT, INSERT

        {'-' * 40}
        """
    print(start_mode)
    warning = f'The document must be located in {file_location}'
    print(cg.color.RED + warning + cg.color.END)


def success(filepath):
    print(cg.color.GREEN + f"Successfully generated document in {filepath}" + cg.color.END)


def failure():
    print(cg.color.RED + "Sorry, an error occurred while generated document" + cg.color.END)


def validating():
    print(cg.color.CYAN + "Validating.. \n" + cg.color.END)


def done_validating():
    print(cg.color.GREEN + "Done Validating" + cg.color.END)
