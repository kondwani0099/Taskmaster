import pyautogui
import cv2
import numpy as np

screen_size = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, screen_size)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

    if cv2.waitKey(1) == 27:  # Esc key to stop recording
        break

out.release()
cv2.destroyAllWindows()
