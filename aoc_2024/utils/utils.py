def get_input(filename: str):
    with open(filename, 'r') as infile:
        return infile.readlines()