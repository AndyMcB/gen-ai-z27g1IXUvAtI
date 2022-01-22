import sqlite3

class DatabaseManager:
    DATABASE_NAME = "weather_data.db"

    def __init__(self):
        pass

    def __get_connection(self):
        return sqlite3.connect(DatabaseManager.DATABASE_NAME)

    def execute_query(self, query_string, query_parameters):
        conn = self.__get_connection()
        cursor = conn.cursor()

        response = {"success":None, "msg":None}        
        try:
            cursor.execute(query_string, query_parameters)
            conn.commit()
        
            response["success"] = True
            response["msg"] = "Success"
        except sqlite3.OperationalError as err:
            response["success"] = False
            response["msg"] = str(err)
        finally:
            conn.close()
        
        return response

    ## Initialization data for application
    def create_tables(self):
        conn = self.__get_connection()
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Sensors
            (id INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL UNIQUE, country TEXT, city TEXT, 
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
            
        cursor.execute('''CREATE TABLE IF NOT EXISTS SensorData
            (id INTEGER PRIMARY KEY AUTOINCREMENT, sensor_uuid TEXT NOT NULL, temperature INT, humidity INT, wind_speed INT, 
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        
        conn.commit()
        conn.close()

    def create_mock_data(self):
        conn = self.__get_connection()
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO Sensors (uuid, country, city)
            values("A1B2C3", "Ireland", "Galway")''')
        cursor.execute('''INSERT INTO Sensors (uuid, country, city)
            values("D4E5F6", "Ireland", "Galway")''')
        cursor.execute('''INSERT INTO Sensors (uuid, country, city)
            values("G7H8I9", "Ireland", "Galway")''')
        cursor.execute('''INSERT INTO Sensors (uuid, country, city)
            values("J10K11", "Ireland", "Dublin")''')
        cursor.execute('''INSERT INTO Sensors (uuid, country, city)
            values("L12M13", "Ireland", "Dublin")''')
        conn.commit()

        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("A1B2C3", "10", "30", "14")''')
        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("A1B2C3", "15", "40", "13")''')
        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("A1B2C3", "20", "50", "9")''')

        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("D4E5F6", "10", "30", "14")''')
        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("D4E5F6", "5", "15", "7")''')
        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("D4E5F6", "2", "5", "2")''')

        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("G7H8I9", "16", "50", "20")''')
        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("G7H8I9", "20", "60", "25")''')
        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("G7H8I9", "22", "70", "30")''')

        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("J10K11", "17", "30", "14")''')
        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("J10K11", "16", "33", "10")''')
        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("J10K11", "12", "36", "9")''')
            
        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("L12M13", "7", "20", "23")''')
        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("L12M13", "5", "10", "25")''')
        cursor.execute('''INSERT INTO SensorData (sensor_uuid, temperature, humidity, wind_speed)
            values("L12M13", "3", "10", "28")''')
        conn.commit()
        
        conn.close()

    


