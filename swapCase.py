def swap_case(string):
    result = ''
    for char in string:
        if char.isupper():
            result = result + char.lower()
        elif char.islower():
            result = result + char.upper()
        else:
            result = result + char

    return result


enter_string = 'adam JONES'
print(swap_case(enter_string))
