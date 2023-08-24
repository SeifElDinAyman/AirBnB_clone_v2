import unittest
import os
import mysql.connector

class TestCreateState(unittest.TestCase):
    def setUp(self):
        # Set up environment variables
        os.environ['HBNB_ENV'] = 'test'
        os.environ['HBNB_MYSQL_USER'] = 'your_username'
        os.environ['HBNB_MYSQL_PWD'] = 'your_password'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'your_test_db'
        os.environ['HBNB_TYPE_STORAGE'] = 'db'

        # Connect to the database and set up initial state
        self.db = mysql.connector.connect(
            host=os.environ['HBNB_MYSQL_HOST'],
            user=os.environ['HBNB_MYSQL_USER'],
            password=os.environ['HBNB_MYSQL_PWD'],
            database=os.environ['HBNB_MYSQL_DB']
        )
        self.cursor = self.db.cursor()
        # Save the initial record count
        self.initial_count = self.get_record_count()

    def tearDown(self):
        # Clean up resources
        self.db.close()

    def get_record_count(self):
        # Helper function to get record count from the database
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        return self.cursor.fetchone()[0]

    def test_create_state_adds_record(self):
        # Define the create state function (replace with your actual function)
        def create_state_function(name):
            # Your function logic here
            pass
        
        # Test the create state function
        create_state_function(name='California')
        updated_count = self.get_record_count()
        # Check if the count increased by 1
        self.assertEqual(updated_count, self.initial_count + 1)

if __name__ == '__main__':
    unittest.main()
