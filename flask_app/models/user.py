#import function to create instance of database
from flask_app.config.mysqlconnection import connectToMySQL
#model the class after the table it represents
class User:
    DB = 'users_schema'
    def __init__(self,data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    #use class methods to call queries
    # CREATE
    @classmethod
    def save(cls,data):
        query = """INSERT INTO users ( first_name,last_name,email )
                VALUES ( %(fname)s, %(lname)s, %(email)s)"""
        return connectToMySQL(cls.DB).query_db(query, data)

    # READ
    @classmethod
    def get_one(cls,id):
        pass

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users" # query string to send to database
        results = connectToMySQL(cls.DB).query_db(query) # actual query call to database
        users = [] # container for all user objects
        for user in results:
            users.append(cls(user)) # creates an instance of User for each db entry
        return users
