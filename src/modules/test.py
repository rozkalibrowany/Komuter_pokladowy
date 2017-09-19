import time

def main2(num,text_edit_box, app):
    for i in range(int(num)):
        text_edit_box.setText(str(i))
        print i
        time.sleep(.1)
        app.processEvents()
    return "success"

def main(num,text_edit_box, app):
    i = 0
    while True:
        text_edit_box.setText(str(i))
        if i%10 == 0:
            i = 0
        i += 1
        time.sleep(.1)
        app.processEvents()
    return "success"

def q():
    quit()
