import cv2
import numpy as np

# 입력 이미지 파일 경로
img_file = "img/dog1.jpg"
# 이미지 읽기
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    #kernel = np.zeros((5, 5), dtype=np.float64) / 25.
    kernel = np.ones((5, 5), dtype=np.float64) / 25
    kernel[0, :] = [-1, -2, -3, -2, -1]
    kernel[1, :] = [-2, -4, -6, -4, -2]
    kernel[2, :] = [0, 0, 0, 0, 0]
    kernel[3, :] = [2, 4, 6, 4, 2]
    kernel[4, :] = [1, 2, 3, 2, 1]

    print(kernel)

    filtered_img = cv2.filter2D(img, -1, kernel)

    cv2.imshow("filtered_img (cv2.filter2D)", filtered_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No image file.")

print('program is terminated')