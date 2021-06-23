# -*- coding: iso-8859-1 -*-
from PIL import Image, ImageDraw, ImageFont
from random import choice


def select_proverbios():
    """Seleciona os proverbios"""
    proverbios1 = (
        (open("proverbios1.txt", "r")).read().replace('\n', ', ').split(', '))
    proverbios_lista1 = []
    proverbios_lista2 = []

    for x in range(len(proverbios1)):
        if (x + 1) % 2 == 0:
            proverbios_lista1.append(proverbios1[x])
        else:
            proverbios_lista2.append(proverbios1[x])

    frase_final = \
        (choice(proverbios_lista2) + ', ' + choice(proverbios_lista1))
    return frase_final

img = Image.new('RGB', (600, 300), color=(73, 109, 137))

fnt = ImageFont.truetype(
    "/usr/share/fonts/TTF/DejaVuSansCondensed-Bold.ttf", 30)
d = ImageDraw.Draw(img)
frase = select_proverbios()
if len(frase) > 35:
    d.text((10, 10), frase[:35], font=fnt, fill=(255, 255, 0))
    d.text((10, 60), frase[35:], font=fnt, fill=(255, 255, 0))
    if len(frase) > 70:
        d.text((10, 10), frase[:70], font=fnt, fill=(255, 255, 0))
fnt = ImageFont.truetype(
    "/usr/share/fonts/TTF/DejaVuSansCondensed-Bold.ttf", 80)
d.text((10, 160), "Bom dia", font=fnt, fill=(255, 255, 0))
img.save('pil_text_font.png')
