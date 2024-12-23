
import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        pass

    def update(self, delta_time):
        self.position += self.velocity * delta_time
        pass

    def split(self):
        self.kill()

        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        angle = random.uniform(20, 50)

        for i in range(2):
            asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid.velocity = self.velocity.rotate(angle if i == 0 else -angle)
            asteroid.velocity *= 1.2



        pass