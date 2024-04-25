import unittest
from flood_fill_algorithm import bfs_fill_flood, main
import os


class TestFillFlood(unittest.TestCase):
    
    def test_flood_fill_with_no_change(self):
        num_rows, num_columns = 4,4
        x, y = 0, 0
        new_color = 'G'
        matrix = [
            ['G', 'G', 'G', 'B'],
            ['R', 'R', 'R', 'B'],
            ['R', 'R', 'R', 'B'],
            ['B', 'B', 'B', 'B']]
        expected_matrix = [
            ['G', 'G', 'G', 'B'],
            ['R', 'R', 'R', 'B'],
            ['R', 'R', 'R', 'B'],
            ['B', 'B', 'B', 'B']
        ]
        self.assertEqual(bfs_fill_flood(num_rows, num_columns, x, y, new_color, matrix), expected_matrix)

    def test_same_color(self):
        num_rows, num_columns = 4,5
        x, y = 1,2
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
        test_directory = os.path.dirname(__file__)
        
        file_input = os.path.join(test_directory, "input.txt")
        file_expected = os.path.join(test_directory, "expected.txt")
        file_output = os.path.join(test_directory, "output.txt")
        main(file_input, file_output)
        with open(file_output, 'r') as file:
            result = [line.strip().split(',') for line in file.readlines()]

        with open(file_expected, 'r') as file:
            expected_result = [line.strip().split(',') for line in file.readlines()]
            
        self.assertEqual(result, expected_result)

    
if __name__ == "__main__":
    unittest.main()
