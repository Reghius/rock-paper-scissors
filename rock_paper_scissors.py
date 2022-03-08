def rock_paper_scissors(a, b):
    possible_moves = ['rock', 'paper', 'scissors']
    if a not in possible_moves or b not in possible_moves:
        return 'Invalid input, try again!'

    if a == b:
        return 'You have a tie'
    elif a == 'rock' and b == 'scissors' or \
            a == 'paper' and b == 'rock' or \
            a == 'scissors' and b == 'paper':
        return 'Player A wins!'
    return 'Player B wins!'


if __name__ == '__main__':
    x = input('Player A, rock, paper or scissors? ')
    y = input('Player B, rock, paper or scissors? ')

    print(rock_paper_scissors(x, y))