# originally by SirCaptainMitch (https://github.com/SirCaptainMitch)

# INTERNAL
from app.ext.Helper import Helper

class Player(object):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, Helper(key, value))

    def set_attr(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, Helper(key, value))




