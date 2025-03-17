def check_pwd(pwd):
    symbols = '~`!@#$%^&()_+-='
    if len(pwd) <= 8 or len(pwd) > 20:
        return False
    if not any(char.isdigit() for char in pwd):
        return False
    if not any(char.isupper() for char in pwd):
        return False
    if not any(char.islower() for char in pwd):
        return False
    if not any(char in symbols for char in pwd):
        return False
    return True
