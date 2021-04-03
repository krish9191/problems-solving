def parent(num):
    def first_child():
        print("Hi, I am Emma")

    def second_child():
        print("Call me Liam")

    if num == 1:
        return first_child
    else:
        return second_child
if __name__ == '__main__':

    parent(1)
