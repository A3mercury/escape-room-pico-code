import board
import digitalio
import ssd1309

sck   = digitalio.DigitalInOut(board.GP2)
sda   = digitalio.DigitalInOut(board.GP3)
dc    = digitalio.DigitalInOut(board.GP4)
reset = digitalio.DigitalInOut(board.GP5)
cs    = digitalio.DigitalInOut(board.GP6)

print("init...")
display = ssd1309.SSD1309_SPI(128, 64, sck, sda, dc, reset, cs)
print("fill white...")
display.fill(0)
display.text("Hello world!", 0, 0)
display.show()
print("done")
