def read_first_five(filename):
    file = open(filename, "r")
    contents = file.read()
    file.close()
    return contents[:5]