import pyodbc as ss


class OpenSS:

    def __init__(self, server, database, username, password):
        # Creating the string that is needed to stabilish a connection with the SQL Server database
        driver = "DRIVER={ODBC Driver 17 for SQL Server};"
        server = f"SERVER={server};"
        database = f"DATABASE={database};"
        username = f"UID={username};"
        password = f"PWD={password};"
        
        connection_string = f"{driver}{server}{database}{username}{password}"

        # Connection
        self.connection = ss.connect(connection_string)

        # Cursor
        self.cursor = self.connection.cursor()

    def __enter__(self):
        # Returning the cursor to the context manager
        return self.cursor

    def __iter__(self):
        # Returning the items fetched by select statements
        for item in self.cursor:
            yield item

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Closing the cursor
        self.cursor.close()
        if isinstance(exc_val, Exception):
            # Rollback if any errors occur
            self.connection.rollback()
        else:
            # Committing the changes if doesn't occur any errors
            self.connection.commit()
        # Closing the connection
        self.connection.close()
