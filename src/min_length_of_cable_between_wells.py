import csv

def find(parents: dict, well: int) -> int:
    """
    Find the root of the set containing the given well using union-find algorithm (disjoint sets).
    Args:
    - parents (dict): A dictionary representing the parent of each well.
    - well (int): The well whose root needs to be found.
    Returns:
    - int: The root of the set containing the given well.
    """
    if parents[well] == well:
        return well
    return find(parents, parents[well])

def union_sets(parents: dict, ranks: dict, well_a: int, well_b: int) -> None:
    """
    Union the sets containing well_a and well_b.
    Args:
    - parents (dict): A dictionary representing the parent of each well.
    - ranks (dict): A dictionary representing the rank of each set.
    - well_a (int): First well.
    - well_b (int): Second well.
    Returns:
    - None
    """
    root_a = find(parents, well_a)
    root_b = find(parents, well_b)

    if root_a != root_b:
        if ranks[root_a] < ranks[root_b]:
            parents[root_a] = root_b
        elif ranks[root_a] > ranks[root_b]:
            parents[root_b] = root_a
        else:
            parents[root_b] = root_a
            ranks[root_a] += 1

def kruskal_mst(edges: list) -> int:
    """
    Calculate the minimum cable length required to connect all wells using Kruskal's algorithm.
    Args:
    - edges (list): A list of triples representing well connections and distances.
    Returns:
    - int: The minimum cable length required. Returns -1 if it's impossible to connect all wells.
    """
    parents, ranks = {}, {}

    for well_a, well_b, _ in edges:
        if well_a not in parents:
            parents[well_a] = well_a
            ranks[well_a] = 0
        if well_b not in parents:
            parents[well_b] = well_b
            ranks[well_b] = 0

    edges.sort(key=lambda item: item[2])

    total_length = 0
    for well_a, well_b, distance in edges:
        root_a = find(parents, well_a)
        root_b = find(parents, well_b)
        if root_a != root_b:
            union_sets(parents, ranks, well_a, well_b)
            total_length += distance

    root_set = find(parents, list(parents.keys())[0])
    for well in parents:
        if find(parents, well) != root_set:
            return -1

    return total_length

def calculate_min_cable_length_from_csv(input_file: str) -> int:
    """
    Read well connections and distances from a CSV file and calculate the minimum cable length required.
    Args:
    - input_file (str): Path to the input CSV file.
    Returns:
    - int: The minimum cable length required. Returns -1 if it's impossible to connect all wells.
    """
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_data = []
        for row in csv_reader:
            csv_data.append(row)

        if len(csv_data) == 0:
            return -1  

        cleaned_csv_data = [[cell.replace('K', '').strip() for cell in row] for row in csv_data]

        graph = [[int(x) for x in row] for row in cleaned_csv_data]

    unique_vertices = set()
    for edge in graph:
        unique_vertices.update(edge[:2])

    return kruskal_mst(graph)