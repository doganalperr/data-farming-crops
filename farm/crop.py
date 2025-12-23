"""
Module: crop
Defines the base Crop class shared by all crops.
"""

# pylint: disable=too-few-public-methods


class Crop:
    """Base class for all crops in the farm."""

    def __init__(self):
        """Initialize a crop with zero grains."""
        self.grains = 0

    def ripe(self):
        """Return True if the crop is ripe (15 or more grains)."""
        return self.grains >= 15
