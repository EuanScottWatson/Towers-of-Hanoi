import pygame, os
from pygame.draw import rect
from pygame.locals import *
import sys
import numpy as np


class Hanoi:
    def __init__(self, n, w, h):
        self.no_pegs = n
        self.w, self.h = w, h

        # inf represents no disc, n represents nth smallest disc
        self.pegs = np.ones((3, n)) * np.inf
        for i in range(n):
            self.pegs[0][i] = n - i

        # Binary number used for solution
        self.binary = [0] * n
    
        self.font = pygame.font.SysFont('Comic Sans MS', 40)

        self.run = False

    def display(self, screen):
        # Function to draw all necessary objects
        gen = self.font.render(" ".join([str(n) for n in self.binary]), False, (0, 0, 0))
        screen.blit(gen, (50, 10))

        for i in range(3):
            base = pygame.Rect(75 + (250 + 50) * i, self.h - 75, 250, 40)
            pygame.draw.rect(screen, (0, 0, 0), base, 0)
            peg = pygame.Rect(195 + (250 + 50) * i, 75, 10, self.h - 150)
            pygame.draw.rect(screen, (0, 0, 0), peg, 0)

        for i, r in enumerate(self.pegs):
            for j, disc in enumerate(r):
                if disc != float('inf'):
                    width = 235 * disc / self.no_pegs + 15
                    height = 30
                    x = 75 + (250 + 50) * i + ((250 - width) // 2)
                    y = self.h - 75 - height - (j * height)
                    base = pygame.Rect(x, y, width, height)
                    pygame.draw.rect(screen, (50, 50, 50), base, 0)

    def events(self):
        # Handles user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
                if event.key == K_SPACE:
                    self.run = not self.run
                if event.key == K_s and not self.run:
                    self.move_peg()

    def display_screen(self, screen):
        screen.fill((160, 160, 169))

        self.display(screen)

        pygame.display.update()
        pygame.display.flip()

    def run_logic(self):
        # Only run if the program isn't paused
        if self.run:
            self.move_peg()

    def move_peg(self):
        if self.pegs[2][-1] == 1 or self.pegs[1][-1] == 1:
            # Stop once the solution is found
            return
        self.binary, disc = self.count(self.binary)

        # Determine the row and column of the current disc to be moved
        r, c = np.where(self.pegs==disc)
        r, c = r[0], c[0]
        self.pegs[r][c] = np.inf

        # Find where it should go next and put it there
        next_smallest = min(self.pegs[(r + 1) % 3])
        cond = next_smallest > disc
        next_r = (r + 1) % 3 if cond else (r + 2) % 3
        next_c = (self.pegs[next_r]==np.inf).argmax(axis=0)
        self.pegs[next_r][next_c] = disc

    def count(self, number):
        # Simple incremementor for binary numbers
        digit = len(number) - 1
        while not all(number):
            if number[digit] == 0:
                number[digit] = 1
                # Return the digit that was toggled to a 1 for the solution
                return number, len(number) - digit
            elif number[digit] == 1:
                number[digit] = 0
                digit -= 1
        return number, -1


def main(towers):
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("")

    os.environ['SDL_VIDEO_CENTERED'] = "True"

    width, height = 1000, 800

    screen = pygame.display.set_mode((width, height))

    done = False
    clock = pygame.time.Clock()
    hanoi = Hanoi(towers, width, height)

    while not done:
        done = hanoi.events()
        hanoi.run_logic()
        hanoi.display_screen(screen)

        clock.tick(2)


if __name__ == "__main__":
    # Default value is 3, otherwise user input limited between 1 and 21
    towers = 3
    if len(sys.argv) == 2:
        try:
            towers = max(1, min(int(sys.argv[1]), 21))
        except:
            print("Incorrect number of towers: %s" % sys.argv[1])
    main(towers)
