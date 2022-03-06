# f = open('girl.txt')
# print(f.read())
# f.close()
# exit
f = open('t.txt')
boy = []
girl = []

for each_line in f:
    (role, line_spoken) = each_line.split(':', 1)
    if role == '男朋友':
        boy.append(line_spoken)
    if role == '女朋友':
        girl.append(line_spoken)

    else:
        file_name_boy = 'boy.txt'
        file_name_girl = 'girl.txt'

        file_boy = open(file_name_boy, 'w')
        file_girl = open(file_name_girl, 'w')

        file_boy.writelines(boy)
        file_girl.writelines(girl)

        file_boy.close()
        file_girl.close()
