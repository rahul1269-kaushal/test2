import pymysql

# database connection
connection = pymysql.connect(host="db-mysql-blr1-30219-do-user-8590280-0.c.db.ondigitalocean.com", user="doadmin",
                             passwd="AVNS_eJl_HHqbl9zQWzxSwWr", database="defaultdb", port=25060)
cursor = connection.cursor()


# inserting data to db
def add_user(email, psw, psw_repeat):
    cursor.execute("INSERT INTO mytable(email, varchar) VALUES (DEFAULT, %s)", email)
    cursor.execute("INSERT INTO mytable(psw, varchar) VALUES (DEFAULT, %s)", psw)
    cursor.execute("INSERT INTO mytable(psw_email, varchar) VALUES (DEFAULT, %s)", psw_repeat)
    connection.commit()
    return 1
