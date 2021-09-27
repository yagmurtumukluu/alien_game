import sys
import pygame


from settings import Settings

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings  = Settings()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")


    def run_game(self):
        #START MAIN LOOP
        while True:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()

                self.screen.fill(self.settings.bg_color)
            # ekranı görünür yap:
            pygame.display.flip()

if __name__ == '__main__':

    ai = AlienInvasion()
    ai.run_game()