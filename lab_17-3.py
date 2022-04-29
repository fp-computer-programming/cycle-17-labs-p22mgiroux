# Author: MOG 4/28/22

import math

class TV_remote:
    """ Circle class represents a circle """

    def __init__(self, channel = 0, volume_level = 0, on = False):
        """ Create a new circle with radius 1 """
        self.channel = channel
        self.volume_level = volume_level
        self.on = on

    def to_string(self):
        if self.on:
            return "The TV is on channel {} on on volume {}.".format(self.channel, self.volume_level)
        else:
            return "The TV is off."

remote = TV_remote(on = True)

print(remote.to_string())