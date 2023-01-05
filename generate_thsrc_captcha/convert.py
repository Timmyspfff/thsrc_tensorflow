import cv2

count = 1
while count < 10001:
    img_grey = cv2.imread("./captcha/%s.png" % count, cv2.IMREAD_GRAYSCALE)

    thresh = 128
    print(count)

    img_binary =cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

    cv2.imwrite("./binary/%s.jpg" % count, img_binary)
    count+=1