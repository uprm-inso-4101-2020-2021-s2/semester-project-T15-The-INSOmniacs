import psycopg2

pg_config = {
    'user': 'daniel',
    'password': 'daniel1',
    'dbname': 'db1',
    'dbport': 8082
}


def connect(self):
    connection_url = "dbname=%s user=%s password=%s port=%s host='localhost'" % (
        pg_config["dbname"],
        pg_config["user"],
        pg_config["password"],
        pg_config["dbport"],
    )
    self.conn = psycopg2.connect(connection_url)
