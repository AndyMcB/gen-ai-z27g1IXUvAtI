from database.manager import DatabaseManager

class Sensor:
    uuid = None
    country = None
    city = None 

    def __init__(self, uuid, country, city):
        self.uuid = uuid
        self.country = country
        self.city = city

    def save(self):
        db_manager = DatabaseManager()
        query_string = "INSERT INTO Sensors (uuid, country, city) values(?, ?, ?)"
        return db_manager.execute_query(query_string, [self.uuid, self.country, self.city])

        
    



