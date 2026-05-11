import pygame
from constants import *
from logger import log_state
from player import *

def main():
    print("Starting Asteroids with pygame version : 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x,y)

        
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for draw in drawable:
            draw.draw(screen)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        player.update(dt)
        dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()
