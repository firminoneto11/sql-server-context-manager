from ss_cm import OpenSS

login_data = {
    "server": "Your server name",
    "database": "Your database name",
    "username": "Your username",
    "password": "Your password"
}

with OpenSS(**login_data) as cursor:
    cursor.execute("Your SQL query here | Select, Insert, Update, Delete")
    for row in cursor:
        print(row)  # Printing each line from a query
