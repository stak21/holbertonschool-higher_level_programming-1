#!/usr/bin/python3
import math


class MagicClass:
    def __init__(self, radius):
        """init
        init method
        """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """circumferencec"""
        return 2 * match.pi * self._MagicClass__radius
