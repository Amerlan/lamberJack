from selenium import webdriver
from PIL import Image, ImageDraw
import time, os, glob

[os.remove(f) for f in glob.glob('log/*.png')]
browser = webdriver.Chrome('chromedriver.exe')
derevo = (161, 116, 56, 255)
browser.get(r'https://tbot.xyz/lumber/#eyJ1IjoxOTkwMTQyNTgsIm4iOiJBbWVybGFuICIsImciOiJMdW1iZXJKYWNrIiwiY2kiOiI2NTAzNzg1NjgwODUwMjA3NTAwIiwiaSI6IkFnQUFBRmh0QkFCeXQ5d0xYdzUxY2owVWNFcyJ9YjkyNGRjMmJjNzUzYWFjNTY1Y2U4MTQ3MjFiZDUwOTU=&tgShareScoreUrl=tg%3A%2F%2Fshare_game_score%3Fhash%3DDaoY5muzHI8q8-snM9SO3emFBEAMeru1VH08HK2QwqA')
browser.find_element_by_class_name("icon_play").click()
browser.save_screenshot('temp.png')
im = Image.open("temp.png")
start_x = 517

right1 = (start_x+50, 170)
left1 = (start_x-50, 170)

sec_right = (start_x+50, 70)
sec_left = (start_x-50, 70)

right3 = (start_x+50, 120)
left3 = (start_x-50, 120)

l_min = r_min = 1000
for i in range(170, 20, -10):
    if im.getpixel((start_x-50, i)) == derevo:
        if i < l_min:
            l_min=i
    if im.getpixel((start_x+50, i)) == derevo:
        if i < r_min:
            r_min=i
print(l_min, r_min)
if l_min > r_min:
    browser.find_element_by_class_name("button_left").click()
    browser.find_element_by_class_name("button_left").click()
    browser.find_element_by_class_name("button_left").click()
    browser.find_element_by_class_name("button_right").click()
    browser.find_element_by_class_name("button_right").click()

else:
    browser.find_element_by_class_name("button_right").click()
    browser.find_element_by_class_name("button_right").click()
    browser.find_element_by_class_name("button_right").click()
    browser.find_element_by_class_name("button_left").click()
    browser.find_element_by_class_name("button_left").click()
# time.sleep(2)
cnt = 0
try:
    while True:
        browser.save_screenshot('temp.png')
        im = Image.open("temp.png")
        if (im.getpixel(left1) == derevo) and (im.getpixel(right3) == derevo):
            browser.find_element_by_class_name("button_right").click()
            browser.find_element_by_class_name("button_right").click()
            browser.find_element_by_class_name("button_left").click()
            browser.find_element_by_class_name("button_left").click()
            print(1)

        if (im.getpixel(right1) == derevo) and (im.getpixel(left3) == derevo):
            browser.find_element_by_class_name("button_left").click()
            browser.find_element_by_class_name("button_left").click()
            browser.find_element_by_class_name("button_right").click()
            browser.find_element_by_class_name("button_right").click()
            print(2)

        if im.getpixel(left1) != derevo:
            browser.find_element_by_class_name("button_left").click()
            browser.find_element_by_class_name("button_left").click()
            browser.save_screenshot('temp.png')
            im = Image.open('temp.png')
            draw = ImageDraw.Draw(im)
            draw.text((10, 50), 'GO LEFT', fill='red')
            im.save('log/'+str(cnt)+'.png')
            cnt += 1

        if im.getpixel(right1) != derevo:
            browser.find_element_by_class_name("button_right").click()
            browser.find_element_by_class_name("button_right").click()
            browser.save_screenshot('temp.png')
            im = Image.open('temp.png')
            draw = ImageDraw.Draw(im)
            draw.text((10, 50), 'GO RIGHT', fill='red')
            im.save('log/' + str(cnt) + '.png')
            cnt += 1

except:
    browser.save_screenshot('result.png')
    time.sleep(1.2)
    browser.close()


# im = Image.open("right.png")
# width, height = im.size
# right = (width//2+50, height//2-120)
# left = (width//2-50, height//2-120)
# drevo = (161, 116, 56, 255)
# draw = ImageDraw.Draw(im)
# for x in range(168, 20, -10):
#     if im.getpixel((width//2+50, x)) != drevo:
#         draw.point((width//2+50, x), fill='red')
#     else:
#         print(x)
#         draw.point((width//2+50, x), fill='black')
# im.save('1.png')
