# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
"""import time
import RPi.GPIO as GPIO

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI


class WS2801Controller:
    def __init__(self):
        self.PIXEL_COUNT = 160
        self.SPI_PORT = 0
        self.SPI_DEVICE = 0
        self.pixels = Adafruit_WS2801.WS2801Pixels(self.PIXEL_COUNT, spi=SPI.SpiDev(self.SPI_PORT, self.SPI_DEVICE),
                                                   gpio=GPIO)

    @staticmethod
    def console_test():
        print("Test")

    def appear_from_back(pixels, color=(255, 0, 0)):
        pos = 0
        for i in range(pixels.count()):
            for j in reversed(range(i, pixels.count())):
                pixels.clear()
                # first set all pixels at the begin
                for k in range(i):
                    pixels.set_pixel(k, Adafruit_WS2801.RGB_to_color(color[0], color[1], color[2]))
                # set then the pixel at position j
                pixels.set_pixel(j, Adafruit_WS2801.RGB_to_color(color[0], color[1], color[2]))
                pixels.show()
                time.sleep(0.02)
"""