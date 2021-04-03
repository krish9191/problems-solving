class LoginUser:
    list_users = []

    def __init__(self, Firstname, Lastname, address, mobile, email, username, password):
        self.f_name = Firstname
        self.l_name = Lastname
        self.add = address
        self.mbl = mobile
        self.email = email
        self.user = username
        self.pwd = password

    def login_check(self, name, password):
        self.u_name = name
        self.u_pwd = password

        for i in log.list_users:

            if i.user == self.u_name and i.pwd == self.u_pwd:
                return f'login successful{i.user}'



if __name__ == '__main__':

    print('for registration TYPE 1')
    print('for sign in TYPE 2')
    print('choose options:')


    x = int(input())
    if x == 1:
        first_name =input('enter your firstname:')
        last_name = input('enter your lastname:')
        address = input('enter your address :')
        phone_no = input('enter your phone number:')
        email = input('enter your email address:')
        username = input('create your username:')
        password = input('create your password:')

        log = LoginUser(first_name, last_name, address, phone_no, email, username, password)
        log.list_users.append(log)

    elif x == 2:
        uname = input('enter your username:')
        upassword = input('enter your password:')
        log1=LoginUser
        log1.login_check('uname','upassword')

