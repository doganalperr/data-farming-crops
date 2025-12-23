"""
Module: corn
Defines the Corn crop.
"""

from farm.crop import Crop


class Corn(Crop):
    """Corn crop that produces grains when watered."""

    def water(self):
        """Water the corn crop and increase grains by 10."""
        self.grains += 10
