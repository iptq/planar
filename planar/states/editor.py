import pygame
import copy
from pygame import Color

import planar.constants as constants
import planar.states as states
from planar.states.end import EndState
from planar.level import Level, Block, Segment
from planar.numinput import InputBox
from planar.textbox import TextBox
from planar.button import Button

class EditorState(states.State):
    def __init__(self, dim):
        seg = Segment(0,0,0,0)
        seg2 = Segment(dim[0]+1,dim[1]+1,0,0)
        level = Level(dim, [
            Block((0,0),[seg,seg2], True, constants.DIRECTION_HORIZONTAL, [1,1,1])
        ], [], [])
        seg.block = level.blocks[0]
        self.level = level
        self.scale = scale = (constants.SCREEN_WIDTH*.66) // (2 * self.level.dim[0] + 6)
        self.yoff = constants.SCREEN_HEIGHT / 2 - (self.level.dim[1] + 4) * self.scale / 2
        xinput = constants.SCREEN_WIDTH*.66
        yinput = self.yoff
        self.cinputs = [InputBox(xinput, yinput-70, 140, 30), InputBox(xinput, yinput-30, 140, 30), \
                        InputBox(xinput, yinput+10, 140, 30)]
        self.texts = [TextBox(xinput, yinput - 100, 120, 20, "New Color"),
                        TextBox(xinput, yinput + 50, 10, 20, "Col:"),
                        TextBox(10, yinput-70, 50, 30, "0"),
                        TextBox(xinput+50, yinput + 50, 100, 20, "None")]
        self.buttons = [Button(xinput+130, yinput-100, 50, 30, "Add", self.add_block),
                        Button(10, yinput-30, 50, 30, "0", self.change_type, val=0),
                        Button(60, yinput-30, 50, 30, "1", self.change_type, val=1),
                        Button(110, yinput-30, 50, 30, "2", self.change_type, val=2),
                        Button(160, yinput-30, 50, 30, "3", self.change_type, val=3),
                        Button(210, yinput-30, 50, 30, "4", self.change_type, val=4),
                        Button(10, 350, 200, 30, "Change Direction", self.change_direction),
                        Button(10, 390, 200, 30, "Change Moveable", self.change_moveable)]
        self.active_block = level.blocks[0]
        self.active_segment = seg

    def to_grid_location(self, pos):
        x = int((pos[0]-2*self.scale)//self.scale)
        y = int((pos[1]-2*self.scale-self.yoff)//self.scale)
        z = 0
        if x > self.level.dim[0]:
            x = int((pos[0] - (4+self.level.dim[0])*self.scale)//self.scale)
            z = 1
        if x < 0 or y < 0 or x >= self.level.dim[0] or y >= self.level.dim[1]:
            return None
        return (x,y,z)

    def change_type(self, type):
        self.active_segment.t = type
        self.texts[2].set_text(type)

    def add_block(self):
        color = [self.cinputs[0].num, self.cinputs[1].num, self.cinputs[2].num]
        for block in self.level.blocks:
            same = True
            for ix in range(len(color)):
                if block.color[ix] != color[ix]:
                    same = False
                    break
            if same:
                return
        seg = copy.deepcopy(self.active_segment)
        pos = seg.position
        seg.rx = 0
        seg.ry = 0
        block = Block(pos, [seg], True, constants.DIRECTION_HORIZONTAL, color)
        block.segments[0].block = block
        self.level.add_block(block)
        xinput = constants.SCREEN_WIDTH*.66
        yinput = self.yoff
        self.buttons.append(
            Button(xinput, yinput+90 + 30 * (len(self.buttons)-8), 100, 30, \
                   str(block.color), self.change_block, color=block.color, val=block)
        )
        self.change_block(block)

    def change_block(self, block):
        self.active_block = block
        self.texts[3].set_text(block.color)

    def change_direction(self):
        self.active_block.direction = constants.opposite(self.active_block.direction)

    def change_moveable(self):
        self.active_block.movable = not self.active_block.movable

    def add_segment(self):
        seg = copy.deepcopy(self.active_segment)
        self.active_block.add_segment(seg)

    def delete_segment(self):
        for block in self.level.blocks:
            result = []
            for seg in block.segments:
                if seg.position != (self.active_segment.rx, self.active_segment.ry) or seg.z != self.active_segment.z:
                    result.append(seg)
            block.segments = result

    def update(self, events):
        for event in events:
            for input in self.cinputs:
                input.handle_event(event)
            for button in self.buttons:
                button.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = self.to_grid_location(pygame.mouse.get_pos())
                if pos != None:
                    (x,y,z) = pos
                    self.active_segment.rx = x
                    self.active_segment.ry = y
                    self.active_segment.z = z
                for block in self.level.blocks:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    self.add_segment()
                if event.key == pygame.K_d:
                    self.delete_segment()

        for input in self.cinputs:
            input.update()
        for text in self.texts:
            text.update()
        for button in self.buttons:
            button.update

    def draw(self, screen):
        screen.fill(Color(100, 80, 100))

        left, right = self.level.render(self.scale)

        if self.active_segment:
            surf = self.active_segment.render(self.scale, [0,0,0])
            (x,y) = self.active_segment.position
            if self.active_segment.z == 0:
                left.blit(surf, (2*self.scale * (1 + x/2), self.yoff + 2*self.scale*(1+y/2)))
            else:
                right.blit(surf, (2*self.scale * (1 + x), self.yoff + 2*self.scale*(1+y)))

        screen.blit(left, (2 * self.scale, self.yoff + 2 * self.scale))
        screen.blit(right, ((4 + self.level.dim[0]) * self.scale, self.yoff + 2 * self.scale))

        for input in self.cinputs:
            input.draw(screen)
        for text in self.texts:
            text.draw(screen)
        for button in self.buttons:
            button.draw(screen)
