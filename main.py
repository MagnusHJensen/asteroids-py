import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    (updatable, drawable, asteroids, shots) = setup_groups()

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    AsteroidField()
    
    delta_time = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        delta_time = game_clock.tick(60) / 1000 # Limit to 60 fps and set delta time in seconds

        # Game logic
        for object in updatable:
            object.update(delta_time)
        
        # Collision detection
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

        # Drawing
        screen.fill((0, 0, 0)) # Black
        for object in drawable:
            object.draw(screen)


        pygame.display.flip()
    pass

def setup_groups():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    return updatable, drawable, asteroids, shots


if __name__ == "__main__":
    main()