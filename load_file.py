def load_file():
    # Does absolutely nothing other than raise the desired exception
    content = open('temp_file.txt')
    if content.length != 0:
        return content
    return None