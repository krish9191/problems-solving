from check_substring import count_substring


def minion_game(string):
    player_a = 0
    player_b = 0
    letter = string
    vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    chk_character = []
    for i in range(len(letter)):
        if letter[i] in vowel:
            char_v = ''
            for k in range(i, len(letter), 1):
                char_v = char_v + letter[k]
                if char_v in chk_character:
                    continue
                else:
                    chk_character.append(char_v)

                player_a += count_substring(string, char_v)
        else:
            char_c = ''
            for k in range(i, len(string), 1):
                char_c = char_c + string[k]
                if char_c in chk_character:
                    continue
                else:
                    chk_character.append(char_c)

                player_b += count_substring(string, char_c)
    if player_a > player_b:
        return f'kevin {player_a}'
    elif player_a < player_b:
        return f'stuart {player_b}'
    else:
        return 'Draw'


if __name__ == '__main__':
    game = minion_game('banana')
    print(game)
