from database.manager import DatabaseManager

def setup():
    db_manager = DatabaseManager()
    db_manager.create_tables()
    db_manager.create_mock_data()

setup()
