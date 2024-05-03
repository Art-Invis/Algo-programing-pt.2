
import unittest
import os
import sys

script_dir = os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.dirname(script_dir))
from src.min_length_of_cable_between_wells import calculate_min_cable_length_from_csv


class MinCableLength(unittest.TestCase):
    def test_random_wells(self):
        result = calculate_min_cable_length_from_csv(
            "D:\\Projects\\Algo-programing-pt.2\\resources\\communication_wells.csv"
        )
        self.assertEqual(result, 3000)

    def test_unconnected_wells(self):
        result = calculate_min_cable_length_from_csv(
            "D:\\Projects\\Algo-programing-pt.2\\resources\\communication_unconnected_wells.csv"
        )
        self.assertEqual(result, -1)

    def test_empty_graph(self):
        result = calculate_min_cable_length_from_csv(
            "D:\\Projects\\Algo-programing-pt.2\\resources\\communication_empty_graphs.csv"
        )
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
