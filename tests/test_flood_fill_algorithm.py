import unittest
import os
import sys

script_dir = os.path.dirname(os.path.relpath(__file__))
sys.path.append(os.path.dirname(script_dir))
from src.flood_fill_algorithm import bfs_fill_flood, run_flood_fill_algorithm

class TestFillFlood(unittest.TestCase):
    
    def test_flood_fill_with_no_change(self):
        num_rows, num_columns = 4, 4
        x, y = 0, 0
        new_color = 'Z'
        matrix = [
            ['G', 'G', 'G', 'B'],
            ['R', 'R', 'R', 'B'],
            ['R', 'R', 'R', 'B'],
            ['B', 'B', 'B', 'B']
        ]
        expected_matrix = [
            ['Z', 'Z', 'Z', 'B'],
            ['R', 'R', 'R', 'B'],
            ['R', 'R', 'R', 'B'],
            ['B', 'B', 'B', 'B']
        ]
        self.assertEqual(bfs_fill_flood(num_rows, num_columns, x, y, new_color, matrix), expected_matrix)

    def test_same_color(self):
        num_rows, num_columns = 4, 5
        x, y = 1, 2
        new_color = 'G'
        matrix = [['G', 'G', 'G', 'G', 'G'],
                  ['G', 'G', 'G', 'G', 'G'],
                  ['G', 'G', 'G', 'G', 'G'],
                  ['G', 'G', 'G', 'G', 'G']]
        expected_matrix = [['G', 'G', 'G', 'G', 'G'],
                           ['G', 'G', 'G', 'G', 'G'],
                           ['G', 'G', 'G', 'G', 'G'],
                           ['G', 'G', 'G', 'G', 'G']]
        self.assertEqual(bfs_fill_flood(num_rows, num_columns, x, y, new_color, matrix), expected_matrix)

    def test_file(self):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        resources_directory = os.path.join(project_root, 'resources')
        
        file_input = os.path.join(resources_directory, "input.txt")
        file_expected = os.path.join(resources_directory, "expected.txt")
        file_output = os.path.join(resources_directory, "output.txt")
        
        run_flood_fill_algorithm(file_input, file_output)
        
        with open(file_output, 'r') as file:
            result = [line.strip().split(',') for line in file.readlines()]

        with open(file_expected, 'r') as file:
            expected_result = [line.strip().split(',') for line in file.readlines()]
            
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()