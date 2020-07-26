from random import choice
from os import system
words = ['word', 'cactus', 'popocatepetl', 'hurmikaki',
         'dragonfruit', 'python', 'goat', 'automation', 'sweigart', 'linux', 'tux', 'amount', 'algebra', 'computer', 'alderson']


class Game:

    def __init__(self):
        self.lives = []
        self.target = list(choice(words))
        self.current = list('_' * len(self.target))
        self.used_letters = []
        for _ in range(len(self.target)):
            self.lives.append('<3')
        self.yourChoice()

    def guess_letter(self):
        self.gui()
        if self.myLetter() == False:
            self.myLetter()
        else:
            if self.my_letter not in self.target:
                self.lives.pop(0)
            else:
                for i in range(len(self.target)):
                    if self.target[i] == self.my_letter:
                        self.current[i] = self.target[i]

    def myLetter(self):
        self.my_letter = input('Your guess: ')
        if 'a' > self.my_letter.lower() or self.my_letter.lower() > 'z' or len(self.my_letter) != 1:
            return False
        else:
            if self.my_letter not in self.used_letters:
                self.used_letters.append(self.my_letter)
            return True

    def yourChoice(self):
        while self.lives != []:
            if '_' in self.current:
                self.guess_letter()
            elif '_' not in self.current:
                self.gui()
                print('\nYou won this one!!!')
                given_word = ''.join(self.target)
                print(f'Your word is "{given_word}"')
                self.nextGame()
        self.gui()
        print('\nYou lost this one :(')
        given_word = ''.join(self.target)
        print(f'You word is "{given_word}"')
        self.nextGame()

    def nextGame(self):
        ans = input('\nDo you want to play another one? [y/N]: ')
        if ans.lower() == 'y':
            game = Game()
        elif ans.lower() == 'n':
            exit()
        else:
            self.nextGame()

    def gui(self):
        system('clear')
        print('Lives: ' + ''.join(self.lives))
        print('Your current word: ' + ''.join(self.current))
        print('Used letters: ' + '-'.join(self.used_letters))


print('\nThis is my take on the Hangman game')
print('If you find any bug, please hit me up at github.com/thekensr')
print('\nHow to play:')
print('\nYour goal is to guess all letters in the given word.')
print('For each successful guess, all guessed letters get uncovered.')
print('For each wrong guess, you lose one heart.')
print('You win if all letters are uncovered, you lose if you have no more hearts.\n')


def start():
    answer = input('Do you want to start your game? [y/N]: ')
    if answer.lower() == 'y':
        if __name__ == '__main__':
            game = Game()
        print('\n')
    elif answer.lower() == 'n':
        exit()
    else:
        start()


start()
