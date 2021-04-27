import psycopg2

pg_config = {
    'user': 'roberto',
    'password': 'Fntasy7',
    'dbname': 'insodb',
    'dbport': 8082,
    'host': "localhost"
}


def connect(self):
    connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % (
        pg_config["dbname"],
        pg_config["user"],
        pg_config["password"],
        pg_config["dbport"],
        pg_config['host']
    )
    self.conn = psycopg2.connect(connection_url)
