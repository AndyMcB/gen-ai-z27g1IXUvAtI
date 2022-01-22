import sqlite3

class DatabaseManager:
    
    def __init__(self):
        pass

    def create_tables(self):
        conn = sqlite3.connect("weather_data.db")
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Sensors
            (id INTEGER PRIMARY KEY AUTOINCREMENT, uuid TEXT NOT NULL, country TEXT, city TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS SensorData
            (id INTEGER PRIMARY KEY AUTOINCREMENT, sensor_uuid TEXT NOT NULL, temperature INT, humidity INT, wind_speed INT)''')
        
        conn.commit()
        conn.close()

    def create_mock_data(self):
        conn = sqlite3.connect("weather_data.db")
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

    


