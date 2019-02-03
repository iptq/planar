import sys

import planar.level as level
import planar.constants as constants
import planar.player as player

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption('test')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

lvl = level.Level((8, 8), [
    level.Block([6,5],[
        level.Segment(0, -1, 0, 2),
        level.Segment(0, 0, 0, 0),
    ], True, constants.DIRECTION_VERTICAL, [255, 10, 100]),
    level.Block([6,3],[
        level.Segment(0, 0, 1, 4),
        level.Segment(-1, 0, 1, 0),
        level.Segment(0, 0, 0, 4),
        level.Segment(-1, 0, 0, 0),
        level.Segment(-2,0,0,2),
        level.Segment(-2,0,1,2)
    ], True, constants.DIRECTION_HORIZONTAL, [0, 255, 100]),
    level.Block([6,2],[
        level.Segment(0, 0, 1, 4),
        level.Segment(0, -1, 1, 0),
        level.Segment(0, 0, 0, 4),
        level.Segment(0, -1, 0, 0)
    ], True, constants.DIRECTION_VERTICAL, [20, 25, 100]),
    level.Block([7,4],[
        level.Segment(0,0,0,0),
        level.Segment(0,0,1,0),
        level.Segment(0,1,0,0),
        level.Segment(0,1,1,0),
        level.Segment(0,2,0,0),
        level.Segment(0,2,1,0),
        level.Segment(0,3,0,0),
        level.Segment(0,3,1,0)
    ], False, 0 , [0,0,0]),
    level.Block([3,5],[
        level.Segment(0,0,0,4),
        level.Segment(0,0,1,4),
        level.Segment(-1,0,0,0),
        level.Segment(-1,0,1,0),
        level.Segment(-2,0,0,0),
        level.Segment(-2,0,1,0)
    ], False, 0 , [110,30,230]),
    level.Block([2,0],[
        level.Segment(0,0,0,0),
        level.Segment(0,0,1,0),
        level.Segment(0,1,0,0),
        level.Segment(0,1,1,0),
        level.Segment(0,2,0,0),
        level.Segment(0,2,1,0),
        level.Segment(0,3,0,0),
        level.Segment(0,3,1,0)
    ], False, 0 , [0,0,0]),
    level.Block([3,5],[
        level.Segment(0,0,0,2),
        level.Segment(0,1,0,0),
    ], False, 0 , [240,50,60]),
    level.Block([3,3],[
        level.Segment(0,0,1,4)
    ], True, constants.DIRECTION_VERTICAL, [120,220,20]),
    level.Block([4,4],[
        level.Segment(0,0,0,0),
        level.Segment(0,0,1,0),
        level.Segment(0,1,0,0),
        level.Segment(0,1,1,0),
        level.Segment(0,2,0,0),
        level.Segment(0,2,1,0),
        level.Segment(0,3,0,0),
        level.Segment(0,3,1,0)
    ], False, 0 , [0,0,0])
], [
    player.Player(5, 5, 0, [66, 134, 244]),
    player.Player(5, 5, 1, [244, 83, 65])
])

lvl.move_block(lvl.blocks[0], constants.DOWN)

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.unicode == 'w':
                lvl.players[0].y -= 1
            elif event.unicode == 'a':
                lvl.players[0].x -= 1
            elif event.unicode == 's':
                lvl.players[0].y += 1
            elif event.unicode == 'd':
                lvl.players[0].x += 1
            elif event.unicode == 'i':
                lvl.players[1].y -= 1
            elif event.unicode == 'j':
                lvl.players[1].x -= 1
            elif event.unicode == 'k':
                lvl.players[1].y += 1
            elif event.unicode == 'l':
                lvl.players[1].x += 1

    screen.blit(background, (0, 0))
    renders = lvl.render(50, 1)
    screen.blit(renders[0], (0, 0))
    screen.blit(renders[1], (50 * 15, 0))
    pygame.display.flip()
