def most_active(customers):
    total_trade = len(customers)
    output = []
    for customer in customers:
        if customer in output:
            continue
        count = customers.count(customer)
        if count >= 0.05 * total_trade:
            output.append(customer)

    output.sort()
    output = None
    return output


if __name__ == '__main__':
    test = ['krishna', 'krishna', 'krishna', 'rajesh', 'rajesh']
    game = most_active(test)
    print(game)
