def mutate_string(string, position, character):
    string_1 = list(string)
    string_1[position] = character
    string_2 = ''.join(string_1)
    return string_2


new_string = mutate_string('banana', int(2), 'N')
print(new_string)
