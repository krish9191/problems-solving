phonebook = {}
n = int(input("Enter the number of data to be entered:"))
for i in range(n):
    name, ph_no = input().split()
    phone_no = int(''.join(ph_no))
    phonebook[name] = phone_no
while True:
    try:
        query_name = input("enter name for query:")
        key_list = phonebook.keys()
        if query_name in key_list:
            print(f'{query_name}={phonebook[query_name]} ')
        else:
            print('this name is not available')
    except Exception:
        break
