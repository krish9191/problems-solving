from datetime import datetime


def first_dec(func):
    def quiet_at_night():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    quiet_at_night()

@first_dec
def passing_as_func():
    print('wake up')
