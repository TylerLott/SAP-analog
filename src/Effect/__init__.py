from abc import ABC


class Effect(ABC):
    """
    Effect Base Class
    """

    def __init__(self):
        self.test = 0

    def __bool__(self):
        return True
