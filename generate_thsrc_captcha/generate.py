import time
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import cv2
import random,string
import csv
import sys
#獲取隨機4個字符組合
# def getRandomChar():
#     chr_all = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"
#     chr_4 = ''.join(random.sample(chr_all,4))
#     return chr_4
#獲取隨機顏色
# def getRandomColor(low,high):
#     # return (random.randint(low,high),random.randint(low,high),random.randint(low,high))
#     return(0,0,0)
#製作驗證碼圖片

count = 0
while(count < 1):
    count+=1
    # file = open('./label.csv','w', encoding = 'utf8', newline = '')
    width,height = 140,48
    ##創建空白畫布
    image = Image.new('RGBA',(width,height),(0,0,0))
    # image.save('./captcha/black.png')
    # img_back = cv2.imread('./captcha/black.png')
    #驗證碼的字體
    font = ImageFont.truetype(r'C:\Users\timmy\code\python\generate_thsrc_captcha\arial-bold.ttf',40)
    #創建畫筆
    draw = ImageDraw.Draw(image)
    #獲取驗證碼
    char_4 = []
    chr_all = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"
    char_4 = ''.join(random.sample(chr_all,4))
    aaa = char_4
    # writer = csv.writer(file)
    # writer.writerows(char_4)
    # file.close()
    # path ='./label.txt'
    # f=open(path,'w')
    # f.write(char_4)
    # f.close()
    # print(char_4)
    #向畫布上填寫驗證碼
    for i in range(4):
        # draw.text((30*i+10,7),char_4[i],font = font)
        draw.text((random.randint(28,33)*i+random.randint(5,7),random.randint(7,10)),char_4[i],font = font)
        # params = [1 - float(random.randint(1, 2)) / 100,
        # 0,0,0,1 - float(random.randint(1, 2)) / 100,
        # float(random.randint(1, 2)) / 500,
        # 0.001,float(random.randint(1, 2)) / 500]
        
        # image = image.transform((140, 48), Image.PERSPECTIVE, params)
        # image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        # fill=getRandomColor(100,200)
    rot= image.rotate(random.randint(-10,10),expand=0)
    fff=Image.new('RGBA',rot.size,(0,)*4)
    image = Image.composite(rot,fff,rot)
    #繪製干擾點
    # for x in range(random.randint(200,600)):
    #     x = random.randint(1,width-1)
    #     y = random.randint(1,height-1)
    #     draw.point((x,y),fill=getRandomColor(50,150))
    #模糊處理
    # image = image.filter(ImageFilter.BLUR)
    # image = cv2.add(image,img_back)
    # cv2.imread(image)
    image.save('./captcha/%s.png' % count)
    # image.save('./captcha/%s.png' % char_4)
    print(aaa)
    # path ='./label.txt'
    # f=open(path,'w')
    # f.writelines(char_4+"\n")
    # f.close()
    # print(char_4)
    # time.sleep(1)
    # return char_4
    
    


# if __name__ == '__main__':
#     getPicture()
#     print(getPicture())

    # with open('./label.txt', 'w') as f:
    #     sys.stdout = f
    # #     sys.stdout = f
    # # csv.writer(sys.stdout)