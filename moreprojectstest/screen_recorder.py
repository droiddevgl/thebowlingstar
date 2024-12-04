import numpy as np
import cv2
from PIL import ImageGrab
from tkinter import *
import threading
import datetime

# Initializing window
window = Tk()
window.title('Screen Recorder')
window.geometry('200x200')
window.resizable(width=False, height=False)
window.configure(bg='black')

frame = Frame(window)
frame.configure(bg='black')
frame.pack()


def starts_recording():
    global recorded
    recorded = not recorded
    resetting_t()

    button_rec_thread = threading.Thread(target=recording())
    thread_counter = threading.Thread(target=display_t())
    thread_screen = threading.Thread(target=screen_recording())

    if recorded:
        button_rec_thread.start()
        thread_counter.start()
    if target == 'screen':
        thread_screen.start()





# Making labels and buttons

button_rec = Button(frame, text='REC', command=starts_recording, font=("Times new roman", 30, "bold"), bg='#e50914',
                    activebackground='#ab070f')
button_rec.grid(row=20, column=2)

timecounter_label = Label(frame, text='0:0:0', font=("Times new roman", 18, "bold"), bg='black', fg='white')
timecounter_label.grid(row=1, column=3)

frame_message = Frame(window)
frame_message.configure(bg='black')
frame_message.pack()
label_message = Label(frame_message, width=3 * 14, bg='black', fg='white')
label_message.pack()

window.mainloop()


def display_t():
    global recorded, secs, mins, hrs
    if recorded:
        if secs == 60:
            secs = 0
            mins += 1
        elif mins == 60:
            mins = 0
            hrs += 1

        timecounter_label.config(text=str(hrs) + ':' + str(mins) + ':' + str(secs))
        secs += 1
        timecounter_label.after(1000, display_t)


def resetting_t():
    global secs, mins, hrs
    secs = 0
    mins = 0
    hrs = 0


# Function for Screen Recording
recorded = False
target = 'screen'
show_preview = True


# Function for recording button
def recording():
    global recorded
    if recorded:
        button_rec['state'] = DISABLED
        label_message['text'] = 'Press ESC to quit.'
    else:
        button_rec['state'] = NORMAL


def screen_recording():
    global show_preview, recorded
    name = 'screen'
    now = datetime.datetime.now()
    date = now.strftime("%H%M%S")
    fileformat = 'mp4'
    filename = name + str(date) + '.' + fileformat
    fps = 24
    resolutions = (1366, 768)
    thumb_resolutions = (342, 192)
    try:
        Four_Char_Code = cv2.VideoWriter.fourcc(*'XVID')
        writer = cv2.VideoWriter(filename, Four_Char_Code, fps, resolutions)
    except cv2.error as e:
        print(f"An error occurred: {e}")

    while True:
        img = ImageGrab.grab()
        np_img = np.array(img)
        frame = cv2.cvtColor(np_img, cv2.COLOR_BGR2RGB)
        writer.write(frame)
        if show_preview:
            thumb = cv2.resize(frame, dsize=thumb_resolutions)
            cv2.imshow('Preview - Screen Recorder', thumb)
        if cv2.waitKey(1) == 27:
            recorded = False
            label_message['text'] = 'Video was saved as ' + filename
            recording()
            break

    writer.release()
    cv2.destroyAllWindows()