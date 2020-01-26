# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
import time
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI


class WS2801Controller:
    def __init__(self):
        self.PIXEL_COUNT = 160
        self.SPI_PORT = 0
        self.SPI_DEVICE = 0
        self.power = False
        self.pixels = Adafruit_WS2801.WS2801Pixels(self.PIXEL_COUNT, spi=SPI.SpiDev(self.SPI_PORT, self.SPI_DEVICE),
                                                   gpio=GPIO)

    @staticmethod
    def change_color(self, color):
        for i in range(self.pixels.count()):
            self.pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(color[0], color[1], color[2]))
            self.pixels.show()

    @staticmethod
    def toggle_power(self):
        self.power = not self.power

    @staticmethod
    def return_power(self):
        return self.power

    @staticmethod
    def power(self):
        if not self.power:
            self.change_color(self, color=(255, 0, 0))
            self.toggle_power()
        else:
            self.pixels.clear()
            self.toggle_power()
