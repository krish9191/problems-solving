def info(**data):
    for key, value in data.items():
        print("{} is {}".format(key, value))


if __name__ == '__main__':
    info(firstname='rajesh', lastname='khadka', age=28, address='93 rue talma')

    info(firstname='krishna', lastname='tiwari', age=29, address='12 rue racine')
