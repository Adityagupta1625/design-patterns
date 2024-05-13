from abc import ABC

class IDatabase(ABC):
    def connect():
        pass

class MySQL(IDatabase):
    def connect(self):
        return "Connected to MYSQL"

class Postgres(IDatabase):
    def connect(self):
        return "Connected to PostgresSQL"

class Application:
    def __init__(self):
        self.database=None
    
    def set_database(self,database):
        self.database=database
    
    def start(self):
        if self.database is not None:
            print(self.database.connect())
        else:
            print("No database set. Please set a database first")

app=Application()
mysql_db = MySQL()
app.set_database(mysql_db)
app.start()

postgres_db = Postgres()
app.set_database(postgres_db)
app.start()

# https://medium.com/coding-becomes-easy/bridge-pattern-48150246e552