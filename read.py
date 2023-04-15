"""import numpy as np
import cv2"""

"""cap = cv2.VideoCapture(0)


while (True):

    # ret is we are returning the variable simple.
    ret, img = cap.read()
    # img = recognize(img, clf, faceCascade)
    cv2.imshow("welcome to face recognization", img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyWindows('img')
cv2.waitKey(1)
cap.release()"""


"""def return_camera_indices():
    index = -2
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr


print(return_camera_indices())"""


"""import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break


cv2.destroyWindows('frame')

# When everything done, release the capture
cap.release()"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyWindow('frame')

# When everything done, release the capture
cap.release()