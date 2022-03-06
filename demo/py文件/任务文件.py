# f = open('D:\\01.txt')
# print(f.read())读取文件内容
# f = open('D:\\t.txt', 'w')
# f.write('不羡慕别人有老公有孩子，不幸福的太多，羡慕那些真心相爱，同心同德的人。希望能找个相互倾慕的人一起变得更好。')
# print(f)
# 女朋友 = girlfriend   男朋友 = Boy friend
f = open('01.txt')

boy = []
girl = []
count = 1

for each_line in f:
    if each_line[:6] !='======':   # 这里进行字符串分割操作 
        (role, line_spoken) = each_line.split(':', 1)
        if role == '男朋友':
            boy.append(line_spoken)
        if role == '女朋友':
            girl.append(line_spoken)
    else:
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'gir_' + str(count) + '.txt'

        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1

file_name_boy = 'boy_' + str(count) + '.txt'
file_name_girl = 'gir_' + str(count) + '.txt'

boy_file = open(file_name_boy, 'w')
girl_file = open(file_name_girl, 'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()

f.close()