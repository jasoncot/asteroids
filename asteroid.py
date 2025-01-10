import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        sub_asteroid_angle_1 = self.velocity.rotate(-random_angle)
        sub_asteroid_angle_2 = self.velocity.rotate(random_angle)

        (x, y) = self.position
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        sub_asteroid_1 = Asteroid(x, y, new_radius)
        sub_asteroid_1.velocity = sub_asteroid_angle_1 * 1.2

        sub_asteroid_2 = Asteroid(x, y, new_radius)
        sub_asteroid_2.velocity = sub_asteroid_angle_2 * 1.2
