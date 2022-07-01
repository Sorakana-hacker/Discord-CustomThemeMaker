import os
import pathlib
from pyfiglet import Figlet

f = Figlet(font='slant')
g = f.renderText('ThemeMaker')
print(g)
h = f.renderText('      By Sorakana')
print(h)
key = input("続行するにはエンターキーを押してください _ _ _")
os.system('cls')

file_name = "CustomTheme.txt"

with open(file_name, encoding="cp932") as f:
    data_lines = f.read()

a = input('ThemeName: ')
data_lines = data_lines.replace("ThemeName", a)
os.system('cls')
b = input('YourName: ')
data_lines = data_lines.replace("YourName", b)
os.system('cls')
c = input('Description: ')
data_lines = data_lines.replace("ThemeDescription", c)
os.system('cls')
d = input('Version: ')
data_lines = data_lines.replace("Ver", d)
os.system('cls')
e = input('YourID: ')
data_lines = data_lines.replace("YourID", e)
os.system('cls')
f = input('Background_URL: ')
data_lines = data_lines.replace("YourURL", f)
os.system('cls')

with open(file_name, mode="w", encoding="cp932") as f:
    f.write(data_lines)

filename = input('FileName: ')
os.rename("CustomTheme.txt", filename) 