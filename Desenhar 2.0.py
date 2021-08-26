#Programado por GM_Senpai

from PIL import Image

import pyautogui as py

from time import sleep

imagem = Image.open('palheta.png')
rgb = imagem.convert('RGB')

sleep(3)


def remove(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


alfa = ''
color=[]
for x in range(303, 810):
    for y in range(145, 562):
        cor = rgb.getpixel((x, y))
        if cor != (255, 255, 255):
            color.append(cor)


lista = remove(color)


for i in lista:
    escala = int((i[0] / 2.55) - 100) * -1
    py.click(233, 407, button='left')
    py.click(427, 436 + escala, button='left')
    py.click(620, 629)
    sleep(1)
    for x in range(303, 810):
        for y in range(145, 562):
            cor = rgb.getpixel((x, y))


            if cor != (255, 255, 255) and i == cor:
                py.click(x, y, button='left')
