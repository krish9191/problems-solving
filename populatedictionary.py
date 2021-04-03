
# T=2
# S='krishna'
# for i in range(T):
#     result1 = S[0:len(S):2]
#     result2 = S[1:len(S):2]
#     result = result1 + ' ' + result2
#     print(result)
phonebook = {}

for i in range(3):

    keys, values = input().split()
    value=int(''.join(values))
    phonebook[keys]=value
while True:
    try:
        query_name=input()
        list1=phonebook.keys()
        if query_name in list1:
            print(f'{query_name}={phonebook[query_name]} ')
        else:
            print('name is not available')
    except:
        break