import cv2

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    if not ret:
        break

    cv2.imshow("Chess Camera", frame)

    key = cv2.waitKey(1)

    if key == ord("s"):
        cv2.imwrite("board.jpg", frame)
        print("Saved board.jpg")

    if key == ord("q"):
        break
