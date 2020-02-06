
def commit_and_close_database(connection):
    connection.commit()
    connection.close()