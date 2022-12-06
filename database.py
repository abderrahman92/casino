import pymysql
import pymysql.cursors

# table: name, level, tries, bet, result


def database_connection():
    db_settings_file = open("db.txt", "r")
    db_settings = db_settings_file.read().splitlines()
    db_settings_file.close()

    try:
        cnx = pymysql.connect(user=db_settings[0], password=db_settings[1],
                              host=db_settings[2], db=db_settings[3])
    except Exception as err:
        print(err)
        exit()
    return cnx


def insert_stats(cnx, username, level, tries, bet, result):
    with cnx.cursor() as cursor:
        query = ("INSERT INTO stats"
                 "(username, level, tries, bet, result)"
                 "VALUES (\"{}\", {}, {}, {}, {})".format(username, level, tries, bet, result))

        cursor.execute(query)
    cnx.commit()


def average_tries(cnx, username, level=0):
    with cnx.cursor() as cursor:
        query = ("SELECT AVG(tries) FROM stats "
                 "WHERE username = \"{}\" {}".format(username, "AND level = " + str(level) if level > 0 else ""))

        cursor.execute(query)
    cnx.commit()

    average = cursor.fetchone()
    return average[0]


def winnings(cnx, username, level=0):
    with cnx.cursor() as cursor:
        query = ("SELECT SUM(bet) FROM stats "
                 "WHERE username = \"{}\" {}".format(username, "AND level = " + str(level) if level > 0 else ""))
        cursor.execute(query)
    cnx.commit()

    winnings = cursor.fetchone()
    return winnings[0]


def scoreboard(cnx):
    with cnx.cursor() as cursor:
        query = ("SELECT DISTINCT "
                 "username as user, "
                 "(SELECT SUM(bet) FROM stats WHERE username = user) as sum, "
                 "(SELECT COUNT(level) FROM stats WHERE level = 1 AND bet >= 0 AND username = user), "
                 "(SELECT AVG(tries) FROM stats WHERE level = 1 AND bet >= 0 AND username = user), "
                 "(SELECT COUNT(level) FROM stats WHERE level = 2 AND bet >= 0 AND username = user), "
                 "(SELECT AVG(tries) FROM stats WHERE level = 2 AND bet >= 0 AND username = user), "
                 "(SELECT COUNT(level) FROM stats WHERE level = 3 AND bet >= 0 AND username = user), "
                 "(SELECT AVG(tries) FROM stats WHERE level = 3 AND bet >= 0 AND username = user) "
                 " FROM stats "
                 "ORDER BY sum DESC "
                 "LIMIT 3")
        cursor.execute(query)
    cnx.commit()

    scores = cursor.fetchall()
    return scores


def delete_account(cnx, username):
    with cnx.cursor() as cursor:
        query = ("DELETE FROM stats WHERE username = \"{}\"".format(username))
        cursor.execute(query)
    cnx.commit()
