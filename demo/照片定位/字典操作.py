
import re
import exifread

# 111, 57, 658493/62500    111 + (658493/62500/60+57)/60
def latitude_and_longitude_convert_to_decimal_system(*args):
    pass

def find_GPS_image(pic_path):
    GPS = {}
    data = ''
    # list = []
    
    with open(pic_path, 'rb')as f:
        ding = exifread.process_file(f)
        for din,value in ding.items():
            pass
            # for value in ding.values():
            
        keys = list(ding.keys())
        values = list(ding.values())
        # d = keys[14:20]
        # print(values)
        # x = values[14]
        # print(x)
        # d2 = {value: key for key, value in ding.items()}
        # for din, value in ding.items():
        
        # data =ding.setdefault('GPS GPSLongitude','it')   #111, 57, 658493/62500



if __name__ == '__main__':
    find_GPS_image('D:/pics/din1.jpg')