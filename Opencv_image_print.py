import cv2
import os

## 파일 경로 확인용
path = os.getcwd()
print(path)

## 경로 한 단계 내려가기
# os.chdir("../")

path = os.getcwd()
print(path)

image = cv2.imread("lunar.png", cv2.IMREAD_ANYCOLOR)
#image = cv2.imread("test2.png", cv2.IMREAD_ANYCOLOR)

cv2.imshow("moon", image)
cv2.waitKey(1000)

## Additional Information
height, width, channel = image.shape
print(height, width, channel)

cv2.destroyAllWindows()