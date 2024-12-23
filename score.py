
import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.score = 0
        self.font = pygame.font.Font(None, 36)


    def add_score(self, score):
        self.score += score

    def draw(self, screen: pygame.Surface):
        text = self.font.render(f"Score: {self.score}", 1, (255, 255, 255))
        screen.blit(text, (10, 10))
        pass