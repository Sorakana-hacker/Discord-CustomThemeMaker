import PySimpleGUI as sg
import os
import pathlib
import shutil
from tkinter import messagebox

sg.theme('TanBlue')

layout = [
    [sg.Text('ThemeMaker  by Sorakana')],
    [sg.Text('ThemeName', size=(13, 1)), sg.InputText('', size=(20, 1), key='theme')],
    [sg.Text('YourName', size=(13, 1)), sg.InputText('', size=(20, 1), key='name')],
    [sg.Text('License', size=(13, 1)), sg.InputText('', size=(20, 1), key='li')],
    [sg.Text('Version', size=(13, 1)), sg.InputText('', size=(5, 1), key='ver')],
    [sg.Text('Background_URL', size=(13, 1)), sg.InputText('', size=(40, 1), key='url')],
    [sg.Text('FileName', size=(13, 1)), sg.InputText('', size=(20, 1), key='file'), sg.Text('.json', size=(7, 1))],
    [sg.Button('Start', key='go'), sg.Button('Cancel', key='no')]
]
     
window = sg.Window('ThemeMaker', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'no':
        break

    if event == 'go': 

        shutil.copyfile("CustomTheme.txt", "Theme1.txt")

        file_name = "Theme1.txt"
        with open(file_name, encoding="cp932") as f:
           data_lines = f.read()

        data_lines = data_lines.replace("ThemeName", values['theme'])
        data_lines = data_lines.replace("YourName", values['name'])
        data_lines = data_lines.replace("li", values['li'])
        data_lines = data_lines.replace("Ver", values['ver'])
        data_lines = data_lines.replace("YourURL", values['url'])

        with open(file_name, mode="w", encoding="cp932") as f:
           f.write(data_lines)

        os.rename("Theme1.txt", values['file']) 

    def change_suffix(file_name, from_suffix, to_suffix):

        sf = pathlib.PurePath(file_name).suffix
        st = pathlib.PurePath(file_name).stem

        to_name = st + to_suffix
        shutil.move(file_name, to_name)

    if __name__ == '__main__':
        change_suffix(values['file'], values['file'], '.json')

        messagebox.showinfo('ThemeMaker', 'Done!                       ')
        ret = messagebox.askyesno('確認', 'ウィンドウを閉じますか？')
    if ret == True:
        sys.exit()
