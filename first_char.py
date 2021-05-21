def str_func(pass_list):
    result = ''
    for item in pass_list:
        temp = item[0]
        result = result + temp
        return result


list_to_pass = ["rajesh", "krishna"]
first_char = map(str_func, list_to_pass)
print(list(first_char))

