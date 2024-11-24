
def is_valid_variable_name(variable_name):
    '''

    Parameters
    ----------
    variable_name : str
        User inputted variable name.

    Returns
    -------
    bool.
    Whether the given string satisfies the naming rules
    True --> satusfactory
    False --> violates rule
    1. Only letters, digits, and underscores
    2. Cannot start with a digit
    3. Must not be a python keyword
    4. No case mixing
    
    
    # A-Z order 65-90
    # a-z order 97-122
    # 0-9 order 48 - 57
    # _ order 95

    '''
    characters = []
    # list of characters in variable_name
    characters[:] = variable_name 
    # list of ord values of characters in variable_name
    ord_characters = list(map(lambda x: ord(x), characters))
    
    # rule 1
    # filters out invalid characters
    # if no invalid characters, list invalid_characters will be empty
    invalid_letters = list(filter(lambda x: not ((48 <= x <= 57) or (65 <= x <= 90) or (97 <= x <= 122) or (x == 95)), ord_characters))
    if len(invalid_letters) > 0:
        return False
    
    # rule 2
    # checks if ord value of first character in variable_name corresponds to a number
    if 45 <= ord_characters[0] <= 57:
        return False
    
    # rule 3
    # checks variable_name against list of key words
    # if variable_name does not match a key work, key_match will be empty
    key_words = ['False', 'None', 'True', 'and', 'as', 'assert', 
                 'async', 'await', 'break', 'class', 'continue', 
                 'def', 'del', 'elif', 'else', 'except', 'finally', 
                 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
                 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
                 'return', 'try', 'while', 'with', 'yield']
    key_match = list(filter(lambda x: x == variable_name, key_words))
    if len(key_match) > 0:
        return False
    
    # rule 4
    # filters out upper and lower case letters
    # if both lists are not empty, then there must be case mixing
    upper_letters = list(filter(lambda x: 65 <= x <= 90, ord_characters))
    lower_letters = list(filter(lambda x: 97 <= x <= 122, ord_characters))
    if (len(upper_letters) > 0) and (len(lower_letters) > 0):
        return False
    
    # if no checks failed, returns True
    return True
    




