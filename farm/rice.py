"""
Module: rice
Defines the Rice crop.
"""
from farm.crop import Crop
class Rice(Crop):
    """Rice crop that produces grains when watered or transplanted."""
    def water(self):
        """Water the rice crop and increase grains by 5."""
        self.grains += 5

    def transplant(self):
        """Transplant the rice crop and increase grains by 10."""
        self.grains += 10
