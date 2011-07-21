# file:    pghelp.py
# author:  Colin Woodbury
# contact: colingw AT gmail
# about:   Libraries for helping out pygame creation.

from random import randrange
import pygame

# STAR RUSH PATTERN
class StarRush():
    '''Lets off a sexy star rush pattern.'''
    angle = 20  # Trajectory of flying stars.

    def __init__(self, starQuant, xOri, yOri, xDim, yDim):
        self.xOri = xOri  # Point where the stars fly from.
        self.yOri = yOri
        self.xDim = xDim  # Dimensions of the window.
        self.yDim = yDim
        # Create stars.
        self.stars = []
        for x in xrange(starQuant):
            xdis = randrange(-self.angle, self.angle)
            ydis = randrange(-self.angle, self.angle)
            colour = random_colour()
            self.stars.append(Star(xOri, yOri, xdis, ydis, colour))

    def draw_and_move(self, screen):
        '''Draws all the stars and moves them once.'''
        for star in self.stars:
            pygame.draw.circle(screen, star.colour, (star.x, star.y), 2)
            pygame.draw.line(screen, star.colour, (star.x, star.y),
                             (star.x - star.xdis*2, star.y - star.ydis*2), 1)
            star.move()
            star.edge_check(self.angle, self.xDim, self.yDim, self.xOri, self.yOri)
            # TEMPORARY - Uncomment for a surprise.
            #self.xOri += 1
            #self.yOri += 1
            #if self.xOri > self.xDim or self.yOri > self.yDim:
            #    self.xOri = 0
            #    self.yOri = 0

class Star():
    '''A cute little star.'''
    def __init__(self, xOri, yOri, xdis, ydis, colour):
        self.x = xOri
        self.y = yOri
        self.xdis = xdis
        self.ydis = ydis
        self.colour = colour

    def move(self):
        '''Moves the star by its y and x dis.'''
        self.x += self.xdis
        self.y += self.ydis

    def edge_check(self, angle, xDim, yDim, xOri, yOri):
        '''Checks if the star is still in the screen.'''
        if not 0 < self.x < xDim or not 0 < self.y < yDim:
            # Return to the middle.
            self.x = xOri
            self.y = yOri
            self.xdis = randrange(-angle, angle)
            self.ydis = randrange(-angle, angle)
            self.colour = random_colour()

# COLOURS
def random_colour():
    '''Generates a random colour.'''
    return (randrange(0, 255), randrange(0, 255), randrange(0, 255))
