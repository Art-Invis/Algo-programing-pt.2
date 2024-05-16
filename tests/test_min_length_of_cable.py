import unittest
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)

from src.min_length_of_cable_between_wells import calculate_min_cable_length_from_csv

class MinCableLength(unittest.TestCase):
    def test_random_wells(self):
        csv_path = "resources/communication_wells.csv"
        result = calculate_min_cable_length_from_csv(csv_path)
        self.assertEqual(result, 3000)

    def test_unconnected_wells(self):
        csv_path = "resources/communication_unconnected_wells.csv"
        result = calculate_min_cable_length_from_csv(csv_path)
        self.assertEqual(result, -1)

    def test_empty_graph(self):
        csv_path = "resources/communication_empty_graph.csv"
        result = calculate_min_cable_length_from_csv(csv_path)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()