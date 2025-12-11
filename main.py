import pygame
import random

pygame.init()


class Game:
    def __init__(self,fen,clock):
        self.coco = pygame.image.load("coco.png")
        self.ana = pygame.image.load("ana.png")
        self.x_coco = 400
        self.y_coco = 500
        self.rect = self.coco.get_rect(x=self.x_coco,y=self.y_coco)
        self.v = 5
        self.fen = fen
        self.clock = clock

        self.obstacles = []
        self.delai_apparition = 0
        self.touche = False
        self.texte = pygame.font.SysFont("comicsansms", 50)
        self.inviincible = 0
    def deplacements(self):
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and self.x_coco > 0:
            self.x_coco -= 5
        elif touches[pygame.K_RIGHT] and self.x_coco < 600:
            self.x_coco += 5
    def apparition_obsacle(self):
        self.delai_apparition += 1
        if self.delai_apparition > 30:
            x = random.choice([100, 200, 300, 400, 500, 600])
            self.obstacles.append([x, -100])
            self.delai_apparition = 0
    def move_obstacles(self):
        for obs in self.obstacles:
            obs[1] += 5
        self.obstacles = [obs for obs in self.obstacles if obs[1] < 600]
    def col(self):
        self.rect = pygame.Rect(self.x_coco, self.y_coco, 100, 100)
        if self.inviincible > 0:
            self.inviincible -= 1
            return False
        self.rect.x, self.rect.y = self.x_coco, self.y_coco
        for obs in self.obstacles[:]:
            rectAna = pygame.Rect(obs[0], obs[1], 80, 80)
            if self.rect.colliderect(rectAna):
                self.v -= 1
                self.obstacles.remove(obs)
                self.inviincible = 60
                return True
        return False
    def dessine(self):
        self.fen.fill((255, 255, 255))
        self.fen.blit(pygame.transform.scale(self.coco, (25, 25)), (self.x_coco, self.y_coco))
        for obs in self.obstacles:
            self.fen.blit(pygame.transform.scale(self.ana, (15,15)), (obs[0], obs[1]))
        affiche = self.texte.render(f"Vies: {self.v}", True, (0, 0, 0))
        self.fen.blit(affiche, (20, 20))
        pygame.display.flip()
        self.clock.tick(60)






pygame.quit()


if __name__ == '__main__':
    print("ok")


