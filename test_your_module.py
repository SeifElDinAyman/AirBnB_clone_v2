import unittest
import mysql.connector
from your_module import create_state_function  # Import your function that creates a state

class TestCreateState(unittest.TestCase):
    def setUp(self):
        # Connect to the database and set up initial state
        self.db = mysql.connector.connect(
            host="localhost",
            user="test_user",
            password="test_password",
            database="test_db"
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
        # Test the create state function
        create_state_function(name='California')
        updated_count = self.get_record_count()
        # Check if the count increased by 1
        self.assertEqual(updated_count, self.initial_count + 1)

if __name__ == '__main__':
    unittest.main()
