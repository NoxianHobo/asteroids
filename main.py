import pygame
import sys

try:
    from .logger import log_state
    from .logger import log_event
    from .constants import *
    from .player import Player
    from .asteroid import Asteroid
    from .asteroidfield import AsteroidField
    from .shot import Shot
except ImportError:
    from logger import log_state
    from logger import log_event
    from constants import *
    from player import Player
    from asteroid import Asteroid
    from asteroidfield import AsteroidField
    from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    log_event("asteroid_hit")
                    print("hit!")
                    asteroid.kill()
                    shot.kill()
                    break

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for sprite in drawable:
            sprite.draw(screen)
        dt = clock.tick(FPS) / 1000.0

        # Game updates should use dt here. Keeping it numeric avoids
        # null/None subtraction bugs in the frame loop.
        pygame.display.flip()


if __name__ == "__main__":
    main()
