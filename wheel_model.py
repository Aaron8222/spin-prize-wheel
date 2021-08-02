"""
Wheel game implementation.
"""

class Screen:
    """
    """
    LENGTH = 650
    HEIGHT = 650
    BACKGROUND_COLOR = 'blue'
    WHEEL_LOCATION = (325,290)
    SPIN_BUTTON_LOCATION = (325,480)
    RIG = 0 # Angle at which you want to land on
   


    def  __init__(self):
        """
        """
        self._wheel_angle = 0
        self._light_on = False
        self._rotation_speed = 0
        self._start_game = False
        


