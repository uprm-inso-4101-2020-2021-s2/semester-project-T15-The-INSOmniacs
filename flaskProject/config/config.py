import psycopg2

pg_config = {
    'user': 'nbxqmuchhkdpff',
    'password': 'c0bd0b9050d8e3eb9a5759d73d33050c2a58d71912557679c9d12fcf4f194ddb',
    'dbname': 'daongl0u0mc566',
    'dbport': 5432,
    'host': "ec2-18-214-140-149.compute-1.amazonaws.com"
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
