def count_substring(string, sub_string):
    count_string = 0
    i = string.find(sub_string)
    while i != -1:
        count_string += 1
        i = string.find(sub_string, i + 1)
    return count_string


if __name__ == '__main__':
    enter_string = input("enter a string:")
    enter_sub_string = input("enter a sub_string:")
    count = count_substring(enter_string, enter_sub_string)
    print(count)
