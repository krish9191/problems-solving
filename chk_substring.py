def count_substring(string, sub_string):
    result = 0

    for i in range(len(string) - 1):
        x = i
        sub_string_result = ''
        for j in range(len(sub_string)):
            if x > len(string) - 1:
                break
            if sub_string[j] != string[x]:
                break
            sub_string_result = sub_string_result + string[x]
            x += 1
            if sub_string_result == sub_string:
                result += 1

    return result


print(count_substring('TestCaseTestCase', 'CaseT'))

# if __name__ == '__main__':
#     string = input().strip()
#
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)
