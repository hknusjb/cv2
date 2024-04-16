

import cv2
#입력 이미지 파일 경로
img_file = "img/dog1.jpg"
# 이미지 읽기
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    blurred_img = cv2.boxFilter(img, -1, (5,5), normalize=True)
# 결과 출력
    cv2.imshow("Blurred Image (cv2.boxFilter)", blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No image file.")

print('program is terminated')