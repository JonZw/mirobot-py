from .mirobot import Mirobot

# don't document our resources directory duh
__pdoc__ = {}
__pdoc__['resources'] = False
__pdoc__['resources.__init__'] = False


# if someone imports by '*' then import everything in mirobot
__all__ = ['mirobot']
