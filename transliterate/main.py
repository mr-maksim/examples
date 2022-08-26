from os import sep
from tkinter.ttk import Separator
from transliterate import translit, slugify

text = "Привет World!"
slug = slugify(translit(text, 'ru', reversed=True), "ru")

print(slug)
