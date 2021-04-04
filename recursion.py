

def deliver_presents_recursively(houses):

    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)

    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]


        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)
if __name__ =='__main__':
    houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]
    deliver_presents_recursively(houses)