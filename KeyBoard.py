import pygame


def display_initiate():
    pygame.init()
    window = pygame.display.set_mode((200, 200))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans


def main():
    if getKey('LEFT'):
        print('Key LEFT was pressed')
    elif getKey('RIGHT'):
        print('Key RIGHT was pressed')
    elif getKey('Up'):
        print('Key UP was pressed')
    elif getKey('DOWN'):
        print('Key DOWN was pressed')


if __name__ == '__main__':
    display_initiate()
    while True:
        main()
