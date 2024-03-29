import numpy
import mss
import cv2
import webbrowser
import pyautogui
import time

url = "https://chromedino.com/"
webbrowser.open(url)

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 395, "left": 220, "width": 10, "height": 10}
    img1 = numpy.array(sct.grab(monitor))
    while "Screen capturing":

        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img2 = numpy.array(sct.grab(monitor))
        if (numpy.any(cv2.absdiff(img1, img2))):  # If there is a difference in image1 and image2 then
            pyautogui.press('up')    # Press space key to jump above cactus

        # Display the picture
        # cv2.imshow("OpenCV/Numpy normal", img1)

        # Display FPS of game
        try:
          print("fps: {}".format(1 / (time.time() - last_time)))
        except:
            print("...")

        img1 = img2

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
