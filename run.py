from layouts import load_layout
from layouts import main_layout
from layouts import select_image_layout
from layouts import  select_video_layout
import PySimpleGUI as gui
import cv2


def main():
    foto = False
    video = False
    webcam = False

    title = 'Age Estimation'

    window = gui.Window(title=title, layout=load_layout())
    window.read(timeout=1000)
    import setup
    window.close()

    window = gui.Window(title=title, layout=main_layout(), element_justification='c')
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            window.close()
            return 0

        if event == 'Foto':
            foto = True
            window.close()
            break

        if event == 'Video':
            video = True
            window.close()
            break

        if event == 'Webcam':
            webcam = True
            window.close()
            break

    if foto:
        window_select_image = gui.Window(title=title + ' - Foto', layout=select_image_layout())
        while True:
            event, values = window_select_image.read()

            if event == gui.WIN_CLOSED:
                window_select_image.close()
                main()
                break

            if event == 'Cancella':
                window_select_image.Element('-SELECT_IMAGE-').Update(value='')
                continue

            if event == 'Seleziona':
                fname = values['-SELECT_IMAGE-']
                if fname == '':
                    gui.popup("Attenzione", "Devi inserire un file per poter andare avanti!")
                    continue
                else:
                    window_select_image.close()
                    window = gui.Window(title=title + ' - Foto', layout=load_layout())
                    window.read(timeout=1000)
                    image = cv2.imread(fname)
                    age_image = setup.classify_age(image)
                    window.close()
                    cv2.putText(age_image, 'Premi \'ESC\' per chiudere', (10, 20), cv2.FONT_ITALIC, 0.5, (0, 0, 0), 1, cv2.LINE_4)
                    while True:
                        cv2.imshow(title + ' - Foto', age_image)
                        if cv2.waitKey(1) == 27:
                            break
            break
        cv2.destroyAllWindows()
        main()


    if video:
        window_select_video = gui.Window(title=title + ' - Video', layout=select_video_layout())
        while True:
            event, values = window_select_video.read()

            if event == gui.WIN_CLOSED:
                window_select_video.close()
                main()
                break

            if event == 'Cancella':
                window_select_video.Element('-SELECT_VIDEO-').Update(value='')
                continue

            if event == 'Seleziona':
                fname = values['-SELECT_VIDEO-']
                if fname == '':
                    gui.popup('Attenzione', 'Devi inserire un file per poter andare avanti!')
                    continue
                else:
                    window_select_video.close()
                    window = gui.Window(title=title + ' - Video', layout=load_layout())
                    window.read(timeout=1000)
                    capture = cv2.VideoCapture(fname)
                    while(capture.isOpened()):
                        window.close()
                        ret, frame = capture.read()
                        cv2.putText(frame, 'Premi \'ESC\' per chiudere', (10, 20), cv2.FONT_ITALIC, 0.5, (0, 0, 0), 1, cv2.LINE_4)
                        if ret == True:
                            age_video = setup.classify_age(frame)
                            cv2.imshow(title + ' - Video', age_video)
                            if cv2.waitKey(1) == 27:
                                break
                        else:
                            break
            break
        capture.release()
        cv2.destroyAllWindows()
        main()

    if webcam:
        window = gui.Window(title=title + ' - Webcam', layout=load_layout())
        window.read(timeout=1000)
        capture = cv2.VideoCapture(0)
        while capture.isOpened():
            window.close()
            ret, frame = capture.read()
            cv2.putText(frame, 'Premi \'ESC\' per chiudere', (10, 20), cv2.FONT_ITALIC, 0.5, (0, 0, 0), 1, cv2.LINE_4)
            if ret == True:
                age_image = setup.classify_age(frame)
                cv2.imshow(title + ' - Webcam', age_image)
                if cv2.waitKey(1) == 27:
                    break
            else:
                break
        capture.release()
        cv2.destroyAllWindows()
        main()


if __name__ == '__main__':
    main()
