import sys

from main import Game
import pygame

pygame.init()

class Menu:
    def __init__(self):
        self.fen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.texte = pygame.font.SysFont('Arial', 20)
        self.jeu = Game(self.fen, self.clock)
        self.quit = [pygame.K_x]
        self.commencer = [pygame.K_LEFT]
        self.alternative = [pygame.K_RIGHT]
        self.run = True
        self.run_menu = True
    def config_menu(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                pygame.quit()
                sys.exit()

            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.lancer_le_jeu()
    def lancer_le_jeu(self):
        self.run = True
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.jeu.deplacements()
            self.jeu.apparition_obsacle()
            self.jeu.move_obstacles()
            if self.jeu.col() and self.jeu.v <= 0:
                self.run = False
            self.jeu.dessine()
            self.clock.tick(60)
    def dessine(self):
        self.fen.fill((255, 255, 255))
        aff = self.texte.render("Séléctionne le bouton : x pour quitter", True, (0,0,0))
        aff2 = self.texte.render("Séléctionne le bouton flêche droite ou gauche pour commencer", True, (0, 0, 0))
        self.fen.blit(aff, (50, 300))
        self.fen.blit(aff2, (50, 350))
        pygame.display.flip()
        self.clock.tick(60)


running_menu = True
menu = Menu()

while running_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_menu = False

        menu.config_menu(event)

    menu.dessine()

pygame.quit()
sys.exit()