class Food:
    def __init__(self, food_type):
        self.food_type = food_type

        self.set_awesomeness()

    def is_awesome(self):
        return 'is awesome'

    def not_awesome(self):
        return 'not awesome'

    # Point to the wanted behavior
    def set_awesomeness(self):
        if self.food_type == 'cookie':
            self.awesomeness = Food.is_awesome()
        else:
            self.awesomeness = Food.not_awesome()

    def get_awesomeness(self):
        return self.awesomeness


cookie = Food('cookie')
cookie.get_awesomeness()  # 'is awesome'

donut = Food('donut')
donut.get_awesomeness()  # 'not awesome'