# f = open('girl.txt')
# print(f.read())
# exit
f = open('t.txt')
boy = []
girl = []
for each_line in f:
    (role, line_spoken) = each_line.split(':',1)
    if role == '男朋友':
        boy.append(line_spoken)
    if role == '女朋友':
        girl.append(line_spoken)

    file_name_boy = 'boy' + '.txt'
    file_name_girl = 'girl' + '.txt'

    boy_file = open(file_name_boy, 'w')
    girl_file = open(file_name_girl, 'w')

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close() 

"""
each_line  表示 每行
role  表示 角色
spoken  表示 说
line  表示 线
file  表示 文件

"""   