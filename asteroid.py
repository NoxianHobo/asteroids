import circleshape
import pygame
import constants
import random
from logger import log_event


class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            constants.LINE_WIDTH,
        )

    def split(self,):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            old_radius = self.radius
            new_radius = old_radius - constants.ASTEROID_MIN_RADIUS
            first_split = Asteroid(self.position.x, self.position.y, new_radius)
            first_split.velocity = self.velocity.rotate(angle)

            second_split = Asteroid(self.position.x, self.position.y, new_radius)
            second_split.velocity = self.velocity.rotate(-angle)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt