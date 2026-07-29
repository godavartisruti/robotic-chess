import cv2

image = cv2.imread("board.jpg")




x1 = 120   
y1 = 35   

x2 = 1120   
y2 = 1045   


cropped = image[y1:y2, x1:x2]


cv2.imshow("Cropped Board", cropped)

cv2.imwrite("cropped_board.jpg", cropped)

print("Saved cropped_board.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()