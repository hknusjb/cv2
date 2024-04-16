import cv2
import matplotlib.pyplot as plt

# 입력 이미지 파일 경로
img_file = "img/dog1.jpg"
# 이미지 읽기
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    gausian_img1 = cv2.GaussianBlur(img, (0, 0), 1)
    gausian_img2 = cv2.GaussianBlur(img, (0, 0), 3)
    gausian_img3 = cv2.GaussianBlur(img, (0, 0), 5)

    plt.subplot(2,2,1)
    plt.title("original")
    plt.imshow(img, cmap='gray')

    plt.subplot(2, 2, 2)
    plt.title("sigma = 1")
    plt.imshow(gausian_img1, cmap='gray')

    plt.subplot(2, 2, 3)
    plt.title("sigma = 3")
    plt.imshow(gausian_img2, cmap='gray')

    plt.subplot(2, 2, 4)
    plt.title("sigma = 5")
    plt.imshow(gausian_img3, cmap='gray')

    plt.show()

    #하나씩 확인
    cv2.imshow("gausian_img1", gausian_img1)  # 읽은 이미지를 화면에 표시 --- ③
    cv2.imshow("gausian_img2", gausian_img2)  # 읽은 이미지를 화면에 표시 --- ③
    cv2.imshow("gausian_img3", gausian_img3)  # 읽은 이미지를 화면에 표시 --- ③
    cv2.waitKey()  # 키가 입력될 때 까지 대기 --- ④
    cv2.destroyAllWindows()  # 창 모두 닫기 --- ⑤


else:
    print("No image file.")


print('program is terminated')