# Built-in imports
#part 1
def reverse(text):
    """
    reverses a string text

    Parameters
    ----------
    text
        a string to be reversed

    Returns
    -------
    str
        a string of the reverse of text

    Example:
    >>>reverse('iamtheking')
    gnikehtmai
    """
    if len(text) > 1:
        x = str(reverse(text[1:]))
        return x + text[0]
    elif len(text) == 1:
        return text[0]
    else:
        return ""
#part 2
def is_palindrome(param):
    """
    takes in a string and examines if string is a palindrome, with spaces and punctuations excluded

    Parameters
    ----------
    param
        a string to be tested if it is a palindrome

    Results
    -------
    bool
        a boolean of True if string is a palindrome and False if string is not a palindrome

    Examples:
    >>>is_palindrome('abba')
    True
    >>>is_palindrome('abc')
    False
    """
    param = str(param)
    lists = []
    for i in param:
        if i.isalpha():
            lists += [i]
    param = ''.join(lists)
    param = str(param).lower()
    if len(param) > 0:
        if param[0] == param[-1]:
            return is_palindrome(param[1:-1])
        else:
            return False
    elif len(param) == 0:
        return True
    return True
reverse(('',))