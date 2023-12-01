# test_slack_data_loader.py
# test_slack_data_loader.py

import unittest
from slack_data_loader import SlackDataLoader

class TestSlackDataLoader(unittest.TestCase):
    def setUp(self):
        # Initialize SlackDataLoader
        self.loader = SlackDataLoader()

    def test_load_data_columns(self):
        # Load data using SlackDataLoader
        df = self.loader.load_data()

        # Define the expected columns
        expected_columns = ['column1', 'column2', 'column3']  # Replace with your expected columns

        # Check if all expected columns are present in the DataFrame
        for column in expected_columns:
            with self.subTest(column=column):
                self.assertIn(column, df.columns)

if __name__ == '__main__':
    unittest.main()

