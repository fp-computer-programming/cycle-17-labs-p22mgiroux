# Author: MOG 4/28/22

import math

class TV_remote:
    """ Circle class represents a circle """

    def __init__(self, channel = 0, volume_level = 0, on = False):
        """ Create a new circle with radius 1 """
        self.channel = channel
        self.volume_level = volume_level
        self.on = on

    def turn_on(self):
        """ Turn the TV on """
        self.on = True
    
    def turn_ooff(self):
        """ Turn the TV off """
        self.on = False

    def volume_up(self):
        """ Turn the volume up """
        self.volume_level += 1
    
    def volume_down(self):
        """ Turn the volume down """
        if self.volume_level != 0:
            self.volume_level -= 1

    def channel_up(self):
        """ Turn the channel up """
        self.channel += 1

    def channel_down(self):
        """ Turn the channel down """
        if self.channel != 0:
            self.channel -= 1
    
    def to_string(self):
        if self.on:
            return "The TV is on channel {} on on volume {}.".format(self.channel, self.volume_level)
        else:
            return "The TV is off."

remote = TV_remote(on = True)

remote.volume_up()

print(remote.to_string())
