import pygame
import copy
from pygame import Color
import json

import planar.constants as constants
import planar.states as states
import planar.serial
from planar.states.end import EndState
from planar.level import Level, Block, Segment
from planar.numinput import InputBox, TextInputBox
from planar.textbox import TextBox
from planar.button import Button
from planar.player import Player

class EditorState(states.State):
    def __init__(self, init_level=None):
        if init_level:
            self.level = init_level
        else:
            self.level = Level((5,5), [], [], [])
        seg = Segment(0,0,0,0)
        self.ghost = Block((0,0),[seg], True, constants.DIRECTION_HORIZONTAL, [1,1,1])
        seg.block = self.ghost
        self.scale = scale = min(int((constants.SCREEN_WIDTH*.66) // (2 * self.level.dim[0] + 6)), \
                                 int((constants.SCREEN_WIDTH*.66) // (2 * self.level.dim[1] + 6)))
        self.yoff = constants.SCREEN_HEIGHT / 2 - (self.level.dim[1] + 4) * self.scale / 2
        xinput = constants.SCREEN_WIDTH*.66
        yinput = self.yoff
        self.filename = TextInputBox(constants.SCREEN_WIDTH*2//5, 20, 100, 30, text="Filename.txt")
        self.cinputs = [InputBox(xinput, yinput-70, 140, 30), InputBox(xinput, yinput-30, 140, 30), \
                        InputBox(xinput, yinput+10, 140, 30)]
        self.dinputs = [InputBox(220, constants.SCREEN_HEIGHT *.75, 200, 30, text="5", minval=1, maxval=16),
                        InputBox(220, constants.SCREEN_HEIGHT *.75+40, 200, 30, text="5", minval=1, maxval=16)]
        self.texts = [TextBox(xinput, yinput - 100, 120, 20, "New Color"),
                        TextBox(xinput, yinput + 50, 10, 20, "Col:"),
                        TextBox(10, yinput-70, 50, 30, "0"),
                        TextBox(xinput+50, yinput + 50, 100, 20, "None")]
        self.buttons = [Button(xinput+130, yinput-100, 50, 30, "Add", self.add_block),
                        Button(10, yinput-30, 50, 30, "0", self.change_type, val=0),
                        Button(70, yinput-30, 50, 30, "1", self.change_type, val=1),
                        Button(130, yinput-30, 50, 30, "2", self.change_type, val=2),
                        Button(190, yinput-30, 50, 30, "3", self.change_type, val=3),
                        Button(250, yinput-30, 50, 30, "4", self.change_type, val=4),
                        Button(10, constants.SCREEN_HEIGHT *.75, 200, 30, "Change Direction", self.change_direction),
                        Button(10, constants.SCREEN_HEIGHT *.75+40, 200, 30, "Change Moveable", self.change_moveable)]
        self.active_block = None
        self.active_segment = seg

        self.ghost_loc = None
        self.ghost_t = 0
        self.states = ["normal"]

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

    def add_player(self):
        (x,y) = self.active_segment.position
        self.level.players.append(Player(x,y,self.active_segment.z, [0,0,0]))

    def add_goal(self):
        (x,y) = self.active_segment.position
        self.level.goals.append((x,y,self.active_segment.z))

    def change_type(self, type):
        self.ghost_t = type
        self.active_segment.t = type
        self.texts[2].set_text(type)

    def add_block(self):
        color = [max(0,min(255,self.cinputs[0].num)), \
                max(0,min(255,self.cinputs[1].num)), \
                max(0,min(255,self.cinputs[2].num))]
        for block in self.level.blocks:
            same = True
            for ix in range(len(color)):
                if block.color[ix] != color[ix]:
                    same = False
                    break
            if same:
                return
        pos = self.active_segment.position
        block = Block(pos, [], True, constants.DIRECTION_HORIZONTAL, color)
        self.level.add_block(block)
        xinput = constants.SCREEN_WIDTH*.66
        yinput = self.yoff
        self.buttons.append(
            Button(xinput, yinput+90 + 35 * (len(self.buttons)-8), 170, 30, \
                   str(block.color), self.change_block, color=block.color, val=block, right=self.delete_block)
        )
        self.change_block(block)

    def change_block(self, block):
        self.active_block = block
        self.texts[3].color = block.color
        self.texts[3].set_text(block.color)

    def delete_block(self, block):
        if self.active_block == block:
            self.active_block = None
            self.texts[3].color = [0,0,0]
            self.texts[3].set_text("None")
        self.level.blocks.remove(block)
        buttons = []
        for button in self.buttons:
            if button.val != block:
                buttons.append(button)
        self.buttons = buttons

    def change_direction(self):
        if not self.active_block:
            return
        self.active_block.direction = constants.opposite(self.active_block.direction)

    def change_moveable(self):
        if not self.active_block:
            return
        self.active_block.movable = not self.active_block.movable

    def add_segment(self):
        if not self.active_block:
            return
        seg = copy.deepcopy(self.active_segment)
        self.active_block.add_segment(seg)
        seg.block = self.active_block

    def delete_segment(self):
        for block in self.level.blocks:
            result = []
            for seg in block.segments:
                if seg.position != (self.active_segment.rx, self.active_segment.ry) or seg.z != self.active_segment.z:
                    result.append(seg)
            block.segments = result
        # delete players and goals too
        players = []
        for player in self.level.players:
            if player.position() != (self.active_segment.rx, self.active_segment.ry, self.active_segment.z):
                players.append(player)
        goals = []
        for goal in self.level.goals:
            if goal != (self.active_segment.rx, self.active_segment.ry, self.active_segment.z):
                goals.append(goal)
        self.level.players = players
        self.level.goals = goals

    def update(self, events):
        self.ghost_loc = self.to_grid_location(pygame.mouse.get_pos())
        if self.ghost_loc:
            self.active_segment.rx = self.ghost_loc[0]
            self.active_segment.ry = self.ghost_loc[1]
            self.active_segment.z = self.ghost_loc[2]
        for event in events:
            for input in self.cinputs:
                input.handle_event(event)
            for input in self.dinputs:
                input.handle_event(event)
            for button in self.buttons:
                button.handle_event(event)
            self.filename.handle_event(event)
            # if event.type == pygame.MOUSEMOTION:
            if event.type == pygame.MOUSEBUTTONDOWN and self.ghost_loc != None:
                # mouse click on the grid
                if event.button == 1:
                    # left click
                    self.add_segment()
                elif event.button == 3:
                    # right click
                    self.delete_segment()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.pop_state()
                if event.key == pygame.K_0 or event.key == pygame.K_5:
                    self.change_type(0)
                if event.key == pygame.K_1:
                    self.change_type(1)
                if event.key == pygame.K_2:
                    self.change_type(2)
                if event.key == pygame.K_3:
                    self.change_type(3)
                if event.key == pygame.K_4:
                    self.change_type(4)
                if event.key == pygame.K_p:
                    self.add_player()
                if event.key == pygame.K_g:
                    self.add_goal()
                if event.key == pygame.K_s:
                    self.save()
                if event.key == pygame.K_l:
                    self.load()

        for input in self.cinputs:
            input.update()
        for input in self.dinputs:
            input.update()
        for text in self.texts:
            text.update()
        for button in self.buttons:
            button.update
        self.filename.update()
        if(self.dinputs[0].text != "" and self.dinputs[1].text != ""):
            self.level.dim = (self.dinputs[0].num, self.dinputs[1].num)
            self.scale = scale = min(int((constants.SCREEN_WIDTH*.66) // (2 * self.level.dim[0] + 6)), \
                                     int((constants.SCREEN_WIDTH*.66) // (2 * self.level.dim[1] + 6)))

    def draw(self, screen):
        screen.fill(Color(100, 80, 100))

        left, right = self.level.render(self.scale)

        # draw the hover segment
        if self.ghost_loc:
            x, y, z = self.ghost_loc
            seg = Segment(x, y, z, self.ghost_t)
            seg.block = self.ghost
            surf = seg.render(self.scale, [100, 200, 250])
            surf.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
            if z == 0:
                left.blit(surf, (self.scale * x + 1, self.scale * y + 1))
            else:
                right.blit(surf, (self.scale * x + 1, self.scale * y + 1))

        screen.blit(left, (2 * self.scale, self.yoff + 2 * self.scale))
        screen.blit(right, ((4 + self.level.dim[0]) * self.scale, self.yoff + 2 * self.scale))

        for input in self.cinputs:
            input.draw(screen)
        for input in self.dinputs:
            input.draw(screen)
        for text in self.texts:
            text.draw(screen)
        for button in self.buttons:
            button.draw(screen)
        self.filename.draw(screen)

    def save(self):
        data = json.dumps(self.level, cls=planar.serial.GameEncoder, indent=2)
        with open(self.filename.text, "w") as fout:
            fout.write(data)

    def load(self):
        self.level = load(self.filename.text)

def load(string):
    with open(string, "r") as fin:
        return json.loads(fin.read(), cls=planar.serial.GameDecoder)
