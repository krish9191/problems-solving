import os
import keyboard


def testfile():
    with open('testfile.txt', 'w+') as test:
        test.write('this is my first file')


if __name__ == '__main__':

    print('1:Edit', '2:NewFile', '3:delete', '4:Rename', '5:open file')
    user_input = int(input('enter no for operation:'))

    if user_input == 1:
        filename = input("enter a filename to be edited:")
        with open(f'{filename}.txt', 'a+') as operation:
            new_text = input('write something in your file')
            operation.write(f'{filename}\r\n{new_text}')

            print('your file has been successfully edited')

    elif user_input == 2:
        file_name = input('enter a file_name:')
        with open(f'{file_name}.txt', 'a+') as operation:
            operation.write(input('write something to the file:'))
            print('your file has been successfully created')

    elif user_input == 3:
        file_name = input('enter a filename to delete:')
        os.remove(f'{file_name}.txt')
        print('your file has been successfully deleted')

    elif user_input == 4:
        old_name = input('enter a old filename:')
        new_name = input('enter a new filename')
        os.rename(f'{old_name}.txt,{new_name}.txt')
        print('your file has been successfully renamed')

    elif user_input == 5:
        file_name = input('enter a file to open:')
        with open(f'{file_name}.txt', 'r') as operation:
            print(operation.read())
