import cv2

image = cv2.imread("cropped1.jpg")

gray = cv2.cvtColor(image)

corners = cv2.goodFeaturesToTrack(
    gray,
    maxCorners=200,
    minDistance=10
)

if corners is not None:
    corners = corners.astype(int)

    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

cv2.imshow("Detected Corners", image)