# pylint: disable=too-few-public-methods


# farm/crop.py



class Crop:
    def __init__(self):
        self.grains = 0

    def ripe(self):
        return self.grains >= 15
