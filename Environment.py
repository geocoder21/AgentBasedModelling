import csv

"""functions to read a csv file (filename) and append values to rowlists
within 2D list (environment), and to write an output file """


def create_environment(filename):
    new_environment = []

    file = open(filename, newline='')
    dataset = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)

    for row in dataset:                     # A list of rows
        rowlist = []
        for value in row:				    # A list of value
            rowlist.append(value)           # Append values to rowlist
            # print(value) 				    # Prints floats
        new_environment.append(rowlist)     # Append rowlist to environment

    file.close()
    return new_environment


def write_environment(environment, filename):
    file = open(filename, 'w', newline='')
    writer = csv.writer(file, delimiter=' ')
    for row in environment:
        writer.writerow(row)    # List of values.
    file.close()
