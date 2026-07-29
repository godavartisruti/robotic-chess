import cv2
import os

image = cv2.imread("cropped_board.jpg")

if image is None:
    print("Couldn't find board.jpg")
    exit()



size = 800

image = cv2.resize(
    image,
    (size, size)
)


square_size = size 


os.makedirs("squares", exist_ok=True)


count = 0


for row in range(8):

    for col in range(8):

        x1 = col * square_size
        y1 = row * square_size

        x2 = x1 + square_size
        y2 = y1 + square_size


        square = image[y1:y2, x1:x2]


        filename = f"squares/square_{row}_{col}.jpg"

        cv2.imwrite(
            filename,
            square
        )


        count += 1


print("Created", count, "squares")


cv2.imshow(
    "Board",
    image
)
