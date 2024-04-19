def is_valid(rows, cols, x, y, previous_color, new_color, matrix_image, visited):
    if x < 0 or x >= rows:
        return False

    if y < 0 or y >= cols:
        return False

    if matrix_image[x][y] == new_color or matrix_image[x][y] != previous_color: 
        return False

    if visited[x][y]:
        return False
    
    return True

def bfs_fill_flood(rows, cols, x, y, new_color, matrix_image):
    previous_color = matrix_image[x][y]

    if previous_color == new_color:
        return matrix_image

    queue = [[x, y]]
    visited = []
    for _ in range(rows):
        visited.append([False] * cols)

    matrix_image[x][y] = new_color

    while queue != []:
        current_pixel = queue.pop(0)
        x_poss, y_poss = current_pixel
        visited[x_poss][y_poss] = True

        if is_valid(rows, cols, x_poss + 1, y_poss, previous_color, new_color, matrix_image, visited):
            matrix_image[x_poss + 1][y_poss] = new_color
            queue.append([x_poss + 1, y_poss])
        if is_valid(rows, cols, x_poss - 1, y_poss, previous_color, new_color, matrix_image, visited):
            matrix_image[x_poss - 1][y_poss] = new_color
            queue.append([x_poss - 1, y_poss])
        if is_valid(rows, cols, x_poss, y_poss + 1, previous_color, new_color, matrix_image, visited):
            matrix_image[x_poss][y_poss + 1] = new_color
            queue.append([x_poss, y_poss + 1])
        if is_valid(rows, cols, x_poss, y_poss - 1, previous_color, new_color, matrix_image, visited):
            matrix_image[x_poss][y_poss - 1] = new_color
            queue.append([x_poss, y_poss - 1])

    return matrix_image

def read_matrix_from_file(file_input):
    with open(file_input, "r") as file:
        read_data = file.readlines()
        rows, cols = map(int, read_data[0].strip().split(','))
        x, y = map(int, read_data[1].strip().split(','))
        new_color = read_data[2].strip()
        matrix_representation = [list(line.strip()) for line in read_data[3:]]
        matrix = [[char for char in row if char.isalpha()] for row in matrix_representation if row]
        return rows, cols, x, y, new_color, matrix


def write_matrix_to_file(matrix, file_output):
    with open(file_output, 'w') as file:
        for row in matrix:
            formatted_row = [f"'{char}'" for char in row]  
            file.write('[' + ', '.join(formatted_row) + ']\n')

    
def main(file_input, file_output):
    rows, cols, x, y, target_color, matrix = read_matrix_from_file(file_input)
    matrix_image = bfs_fill_flood(rows, cols, x, y, target_color, matrix)
    write_matrix_to_file(matrix_image, file_output)
