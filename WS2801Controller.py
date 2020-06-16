# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI


class WS2801Controller:
    PIXEL_COUNT = 160
    SPI_PORT = 0
    SPI_DEVICE = 0
    powerFlag = False
    pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE),
                                          gpio=GPIO)

    @staticmethod
    def changeColor(color):
        print(color)
        WS2801Controller.applyColor(WS2801Controller, color=color)
        
    @staticmethod
    def applyColor(self, color):
        for i in range(self.pixels.count()):
            self.pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(color[0], color[1], color[2]))
        self.pixels.show()

    @staticmethod
    def togglePower():
        WS2801Controller.powerFlag = not WS2801Controller.powerFlag

    @staticmethod
    def power():
        if not WS2801Controller.powerFlag:
            WS2801Controller.applyColor(WS2801Controller, color=(204, 0, 204))
            WS2801Controller.togglePower()
        else:
            WS2801Controller.pixels.clear()
            WS2801Controller.pixels.show()
            WS2801Controller.togglePower()
