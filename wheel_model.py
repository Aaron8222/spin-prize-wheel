"""
Wheel game implementation.
"""

class Screen:
    """
    """
    LENGTH = 600
    HEIGHT = 600
    BACKGROUND_COLOR = 'blue'
    WHEEL_LOCATION = (300,300)
    SPIN_BUTTON_LOCATION = (300,500)
    RIG = 0 # Angle at which you want to land on
   


    def  __init__(self):
        """
        """
        self._wheel_angle = 0
        self._light_on = False
        self._rotation_speed = 0
        


