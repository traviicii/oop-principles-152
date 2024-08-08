import os

def d():
    '''Creates a divider in terminal'''
    print('=' * 75)

def fancy():
    '''Creates a fancier divider in terminal'''
    print('~' * 50)

def clear():
    '''Clear the terminal contents'''
    os.system('cls' if os.name == 'nt' else 'clear')