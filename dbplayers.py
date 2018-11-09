import psycopg2

conn = psycopg2.connect('dbname=golfscores')
cur = conn.cursor()

def get_player_names ():
    query = """
            select *
            FROM
            players
            """

    cur.execute(query)

    something = cur.fetchall()

    return something

def get_single_player_name (player_id):
    query = """
            select first_name last_name
            FROM
            players
            where
            player_id = %s
            """

    values = (player_id,)
    
    cur.execute(query, values)

    something = cur.fetchall()

    return something