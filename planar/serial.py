import json
import pygame

from planar.level import Segment, Block, Level
from planar.player import Player

class GameEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Segment):
            return {
                "type": "segment",
                "rx": obj.rx,
                "ry": obj.ry,
                "z": obj.z,
                "t": obj.t,
            }
        elif isinstance(obj, Player):
            return {
                "type": "player",
                "x": obj.x,
                "y": obj.y,
                "z": obj.z,
                "color": obj.color,
            }
        elif isinstance(obj, Block):
            return {
                "type": "block",
                "x": obj.x,
                "y": obj.y,
                "segments": obj.segments,
                "movable": obj.movable,
                "direction": obj.direction,
                "color": obj.color,
            }
        elif isinstance(obj, Level):
            return {
                "type": "level",
                "w": obj.dim[0],
                "h": obj.dim[1],
                "blocks": obj.blocks,
                "players": obj.players,
                "goals": obj.goals,
            }
        return super().default(obj)

class GameDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if "type" in obj:
            t = obj["type"]
            if t == "segment":
                return Segment(obj["rx"], obj["ry"], obj["z"], obj["t"])
            elif t == "block":
                return Block((obj["x"], obj["y"]), self.object_hook(obj["segments"]), obj["movable"], obj["direction"], obj["color"])
            elif t == "level":
                return Level((obj["w"], obj["h"]), self.object_hook(obj["blocks"]), self.object_hook(obj["players"]), obj["goals"])
            elif t == "player":
                return Player(obj["x"], obj["y"], obj["z"], obj["color"])
        return obj
