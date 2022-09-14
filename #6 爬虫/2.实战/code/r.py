from selenium import webdriver
import time
import re

driver = webdriver.Chrome()

driver.get('https://item.jd.com/100019125569.html')
driver.maximize_window()
time.sleep(5)
driver.execute_script("window.scrollTo(0,1680)")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.find_element("xpath", '//*[@id="detail"]/div[1]/ul/li[5]').click()
time.sleep(3)
page = 2
driver.find_element("xpath", '//*[@id="comment-0"]/div[12]/div/div/a[' + str(page) + ']').click()

time.sleep(1)
count = 0
collectCount = 1
page = 2
time.sleep(5)
run = 0

while run < 51:
    page = 1 + page
    while count < 10:
        username = driver.find_element("xpath",
                                       '//*[@id="comment-0"]/div[' + str(collectCount) + ']/div[1]/div[1]').text
        test = driver.find_element("xpath", '//*[@id="comment-0"]/div[' + str(collectCount) + ']/div[2]').text

        # 清洗
        out = test.replace('取消静音', '').replace('Current Time', '').replace('0:00', '').replace('时长', '').replace(
            '加载完毕: 0%', '').replace('进度: 0%', '').replace('播放视频', '').replace('播放', '').replace(' 全屏', '').replace('当前时间','')
        pattern0 = re.compile('举报 \d \d', re.S)
        pattern1 = re.compile('举报 \d\d \d', re.S)
        pattern2 = re.compile('举报 \d \d\d', re.S)
        pattern3 = re.compile('举报 \d\d \d\d', re.S)
        pattern4 = re.compile('举报 \d\d\d \d', re.S)
        pattern5 = re.compile('举报 \d\d\d \d\d', re.S)
        pattern6 = re.compile('举报 \d\d\d \d\d\d', re.S)
        pattern7 = re.compile('举报 \d \d\d\d', re.S)
        pattern8 = re.compile('举报 \d\d \d\d\d', re.S)
        pattern9 = re.compile('0:\d\d', re.S)

        out1 = pattern0.sub('', out)
        out2 = pattern1.sub('', out1)
        out3 = pattern2.sub('', out2)
        out4 = pattern3.sub('', out3)
        out5 = pattern4.sub('', out4)
        out6 = pattern5.sub('', out5)
        out7 = pattern6.sub('', out6)
        out8 = pattern7.sub('', out7)
        out9 = pattern8.sub('', out8)
        out10 = pattern9.sub('', out9)

        #print(username)
        #print(out9)
        with open('output.txt', 'a', encoding='utf-8') as f:
            f.write(f'{username}')
            f.write("\n")
            f.write(f'{out10}')
            f.write("\n")

        count = 1 + count
        collectCount = 1 + collectCount
    driver.find_element("xpath", '//*[@id="comment-0"]/div[12]/div/div/a[8]').click()
    # //*[@id="comment-0"]/div[12]/div/div/a[8]
    #//*[@id="comment-0"]/div[12]/div/div/a[8]
    #//*[@id="comment-0"]/div[12]/div/div/a[8]

    # *[ @ id = "comment-0"] / div[12] / div / div / a[8]
    #driver.find_element("xpath", '//*[@id="comment-0"]/div[12]/div/div/a[' + str(page) + ']').click()
    count = 0
    collectCount = 1
    time.sleep(5)
    run = 1 + run
# 9 //*[@id="comment-0"]/div[12]/div/div/a[6]
#
# //*[@id="comment-0"]/div[12]/div/div/a[6]
# //*[@id="comment-0"]/div[12]/div/div/a[6]
# //*[@id="comment-0"]/div[12]/div/div/a[6]
# //*[@id="comment-0"]/div[12]/div/div/a[7]
# //*[@id="comment-0"]/div[12]/div/div/a[6]
# //*[@id="comment-0"]/div[12]/div/div/a[6]

driver.close()
