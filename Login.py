from PIL import ImageGrab
from pyautogui import press
from pyautogui import click
from time import sleep

nick = input('Seu nick: ')

sleep(3)

while True:

    tela = ImageGrab.grab()
    if tela.getpixel((31, 445)) == (0, 129, 255):
        exit()
    click(x=662, y=421, button='left')
    for letra in range(len(nick)):
        press(nick[letra])
    press('enter')
    if tela.getpixel((31, 445)) != (0, 129, 255):
        sleep(5)
        click(x=678, y=433, button='left')
