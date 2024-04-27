import keyboard
import turtle

cherepaha = turtle.Turtle()

while True:
    if keyboard.is_pressed("w"):
        cherepaha.forward(10)
    elif keyboard.is_pressed("a"):
        cherepaha.left(5)
    elif keyboard.is_pressed("d"):
        cherepaha.right(5)
    elif keyboard.is_pressed("s"):
        cherepaha.back(5)
    elif keyboard.is_pressed("esc"):
        break

cherepaha.done