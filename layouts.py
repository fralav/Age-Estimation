import PySimpleGUI as gui

gui.theme('Reddit')


def load_layout():
    layout = [
        [gui.Text('Caricamento in corso...', size=(40, 10), justification='c')]
    ]
    return layout


def main_layout():
    layout = [
        [gui.Text('Effettua la tua scelta', size=(40, 2), justification='c')],
        [gui.Button('Foto', size=(20, 2), tooltip='Stima l\'età di uno o più volti da un file immagine.')],
        [gui.Button('Video', size=(20, 2), tooltip='Stima l\'età di uno o più volti da un file video.')],
        [gui.Button('Webcam', size=(20, 2), tooltip='Stima l\'età di uno o più volti dal flusso webcam.')]
    ]
    return layout


def select_image_layout():
    layout = [
        [gui.Text('Seleziona un file immagine:')],
        [gui.In(key='-SELECT_IMAGE-', disabled=True), gui.FileBrowse(button_text='Sfoglia', file_types=(('Formato immagine', '*.bmp'), ('Formato immagine', '*.dib'), ('Formato immagine', '*.jpe'), ('Formato immagine', '*.jpeg'), ('Formato immagine', '*.jpg'), ('Formato immagine', '*.jp2'), ('Formato immagine', '*.pbm'), ('Formato immagine', '*.png')))],
        [gui.Open(button_text='Seleziona'), gui.Cancel(button_text='Cancella')]
    ]
    return layout

def select_video_layout():
    layout = [
        [gui.Text('Seleziona un file video:')],
        [gui.In(key='-SELECT_VIDEO-', disabled=True), gui.FileBrowse(button_text='Sfoglia', file_types=(('Formato video', '*.avi'), ('Formato video', '*.mp4'))), ],
        [gui.Open(button_text='Seleziona'), gui.Cancel(button_text='Cancella')]
    ]
    return layout