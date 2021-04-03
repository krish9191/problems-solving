class Food:
    def __init__(self,food_type):
        self.food_type = food_type

        if self.food_type == 'cookie':
            print('this is a cookie')

    def is_awesome(self):
        print("is awesome")
    #     else:
    #         print('this is not a cookie')
    # def is_awesome(self):
    #     print("not awesome")
food=Food('cookie')
food.is_awesome()