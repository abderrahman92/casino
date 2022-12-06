import pymysql
import pymysql.cursors

# table: name, level, tries, bet, result, gain


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


def insert_stats(cnx, username, level, tries, bet, result, gain):
    with cnx.cursor() as cursor:
        query = ("INSERT INTO stats"
                 "(username, level, tries, bet, result, gain)"
                 "VALUES (\"{}\", {}, {}, {}, {}, {})".format(username, level, tries, bet, result, gain))

        cursor.execute(query)
    cnx.commit()

    return cursor.lastrowid 


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
        query = ("SELECT SUM(gain) FROM stats "
                 "WHERE username = \"{}\" {}".format(username, "AND level = " + str(level) if level > 0 else ""))
        cursor.execute(query)
    cnx.commit()

    winnings = cursor.fetchone()
    return winnings[0]


def scoreboard(cnx):
    with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
        query = ("SELECT DISTINCT "
                 "username as user, "
                 "(SELECT SUM(gain) FROM stats WHERE username = user) as sum, "
                 "(SELECT COUNT(level) FROM stats WHERE level = 1 AND gain >= 0 AND username = user) as win_level_1, "
                 "(SELECT AVG(tries) FROM stats WHERE level = 1 AND gain >= 0 AND username = user) as average_tries_level_1, "
                 "(SELECT COUNT(level) FROM stats WHERE level = 2 AND gain >= 0 AND username = user) as win_level_2, "
                 "(SELECT AVG(tries) FROM stats WHERE level = 2 AND gain >= 0 AND username = user) as average_tries_level_2, "
                 "(SELECT COUNT(level) FROM stats WHERE level = 3 AND gain >= 0 AND username = user) as win_level_3, "
                 "(SELECT AVG(tries) FROM stats WHERE level = 3 AND gain >= 0 AND username = user) as average_tries_level_3, "
                 "(SELECT MAX(level) FROM stats WHERE gain >= 0 AND username = user) as max_level_won, "
                 "(SELECT COUNT(*) FROM stats WHERE level = 1 AND tries = 1 AND username = user) as first_try_win, "
                 "(SELECT MAX(gain) FROM stats WHERE username = user) as max_gain, "
                 "(SELECT COUNT(*)/(SELECT COUNT(*) FROM stats WHERE username = user) FROM stats WHERE gain >= 0 AND username = user) as win_percentage "
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


def insert_play(cnx, stat_id, choices):
    with cnx.cursor() as cursor:
        for choice in choices:
            query = ("INSERT INTO user_play"
                     "(stats_id, play)"
                     "VALUES ({}, {})".format(stat_id, choice))
            cursor.execute(query)
    cnx.commit()
