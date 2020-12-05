for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j," ",end="")
    print()
#How to print the time
import time
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(2)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print(time.localtime())

import datetime


# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print(datetime.date.today().strftime('%d/%m/%Y'))

# 创建日期对象
miyazakiBirthDate = datetime.date(1941, 1, 5)

print(miyazakiBirthDate.strftime('%d/%m/%Y'))

    # 日期算术运算
miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)

print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))


s = str(input('请输入一个字符串:\n'))
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))