from machine import Pin
import neopixel as n
import random
from time import sleep

#funcion que asigna un color aleatorio a cada led
def random_color(led_index, pixels):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    #escribir nuevo color en led
    #Para cada led, los colores se representan en (Rojo, Azul, Verde)
    pixels[led_index] = (r,g,b)
    return pixels

#codigo principal de programa
def main():
    #definir pin de salida para arreglo de leds
    pixels = n.NeoPixel(Pin(4, Pin.OUT), 3)
    while(True):
        #cada linea corresponde a un unico led
        pixels = random_color(0, pixels) #asignar color aleatorio a led 1
        pixels = random_color(1, pixels) #asignar color aleatorio a led 1
        pixels = random_color(2, pixels) #asignar color aleatorio a led 1
        pixels.write() #mostrar color
        sleep(0.5)
        
#ruta de ejecucion
if __name__ == "__main__":
    main()
