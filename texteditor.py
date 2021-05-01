import os
import keyboard



def testfile():
    test = open('testfile.txt', 'w+')
    test.write('this is my first file\n')
    test.close()





if __name__ == '__main__':

    print('1:Edit', '2:NewFile', '3:delete', '4:Rename', '5:open file')
    user_input = int(input('enter no for operation:'))

    if user_input == 1:
        new_text = list()
        new_text.append(input('enter new lines:'))
        if keyboard.is_pressed('enter'):


        operation = open('testfile.txt', 'a')
        operation.write(new_text[0])
        print('your file has been successfully edited')



    elif user_input == 2:
        file_name = input('enter a file_name:')
        operation = open(f'{file_name}.txt', 'w')
        new_text = list()
        new_text.append(input('enter lines to be saved'))
        operation.write(new_text[0])
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
        operation = open(f'{file_name}.txt', 'r')
        print(operation.read())
