import cv2
import os


before_folder = "before"
after_folder = "after"


changed = []


for row in range(8):
    for col in range(8):

        before_path = f"{before_folder}/square_{row}_{col}.jpg"
        after_path = f"{after_folder}/square_{row}_{col}.jpg"

        before = cv2.imread(before_path)
        after = cv2.imread(after_path)


        if before is None or after is None:
            print("Missing image:", row, col)
            continue


        # compare images
        difference = cv2.absdiff(before, after)

        # total amount of change
        score = difference.sum()

        print(row, col, score)
        if score > 50000:
            changed.append((row, col, score))


print("\nChanged squares:")

for square in changed:
    print(square)