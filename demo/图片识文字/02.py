from aip import Aipocr

from config import config
client = Aipocr(**config)

# 获取图像
def get_file_content(file):
    with open(file,'rb')as f:
        return f.read()

# 把图片里文字识别出来
def img_to_str(imge_path):
    imge = get_file_content(imge_path)
    # client.basicGeneral(imge)
    result = client.handwriting(imge)
    # print(result)
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])