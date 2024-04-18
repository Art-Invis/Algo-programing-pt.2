def make_matrix_of_preferences(num_employees, num_beers, preferences_str):
    preference_matrix = []
    preferences = preferences_str.split()
    
    for preference in preferences:
        employee_preferences = []
        for pref in preference:
            if pref == 'Y':
                employee_preferences.append(1)
            else:
                employee_preferences.append(0)

        preference_matrix.append(employee_preferences)

    if len(preference_matrix) == num_employees:
        pass

    return get_least_preferred_row(preference_matrix, num_beers)

def all_zeros(row):
    return all(preference == 0 for preference in row)

def get_least_preferred_row(matrix, num_of_beers):
    least_preferred_row = None
    least_num_beers = num_of_beers
    
    for row in matrix:
        if all_zeros(row):
            continue

        num_pref_in_row = sum(row)
        
        if num_pref_in_row <= least_num_beers:
            least_num_beers = num_pref_in_row
            least_preferred_row = row

    if least_preferred_row is None:
        return 0

    return get_min_num_of_beers(matrix, num_of_beers, least_preferred_row)

def get_min_num_of_beers(matrix, num_of_beers, least_preferred_row):
    num_beers = 1
    row_length = num_of_beers
    
    for row in matrix:
        if all_zeros(row) or row == least_preferred_row:
            continue

        for i in range(row_length):
            if row[i] == 1 and least_preferred_row[i] == 1:
                break
        else:
            num_beers += 1
            for j in range(row_length):
                if row[j] == 1:
                    least_preferred_row[j] = 1
                    break
    return num_beers
