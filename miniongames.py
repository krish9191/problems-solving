def minion_game(string):
    player_a=0
    player_b=0

    vowel=('a','e','i','o','u','A','E','I','O','U')
    lst1=list(string)

    chklist=[]

    for i in range(len(lst1)):
        if lst1[i] in vowel:
            str=''
            for k in range(i,len(lst1),1):
                str = str + lst1[k]
                if str in chklist:
                    continue
                else:
                    chklist.append(str)
                j = string.find(str)
                while j != -1:
                    player_a += 1
                    j = string.find(str, j + 1)


        else:
            str1=''
            for k in range(i,len(lst1),1):
                    str1 = str1 + lst1[k]
                    if str1 in chklist:
                        continue
                    else:
                        chklist.append(str1)
                    j = string.find(str1)
                    while j != -1:
                        player_b += 1
                        j = string.find(str1, j + 1)

    if player_a > player_b:
        return f'kevin {player_a}'
    elif player_a<player_b:
        return f'stuart {player_b}'

    else:
        return 'Draw'





if __name__ == '__main__':
    x = minion_game('abbaas')
    print(x)
