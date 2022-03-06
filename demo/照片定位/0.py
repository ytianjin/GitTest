from multiprocessing.sharedctypes import Value
import re
from telnetlib import PRAGMA_HEARTBEAT
from tkinter import N
import exifread
from numpy import NaN
                          #111.952927                       22.7448997
# 111, 57, 658493/62500    111 + (658493/62500/60+57)/60   22, 44, 41639099/1000000   22+44/60+41639099/1000000/3600
def latitude_and_longitude_convert_to_decimal_system(*args):
    pass

def find_GPS_image(pic_path):
    GPS = {}

    with open(pic_path, 'rb')as f:
        ding = exifread.process_file(f)
        Longitude_key,Latitude_key = 'GPS GPSLongitude','GPS GPSLatitude'
        a = ding.get('GPS GPSLongitudeRef')
        b = str(ding.get('GPS GPSLongitude')).replace('[','').replace(']','')
        print(b)
        # c= str(b).replace('[','').replace(']','')

        # print(GPS)
        # if Longitude_key in ding.keys():
        #     Longitude_val = ding[Longitude_key].values
        #     print(Longitude_val)
        # Longitude_key = 'GPS GPSLongitudeRef'
        # a = ding['GPS GPSLongitudeRef']
        # longitude_valu = 'GPSLongitude' 'GPS GPSLongitudeRef': (0x0003) ASCII=E @ 9012, 'GPS GPSLongitude': (0x0004)
        # b = ding['GPS GPSLongitude']
        # print(b)
        # Longitude_key,Latitude_key = 'GPS GPSLongitudeRef','GPS GPSLatitudeRef',ding['GPS GPSLongitudeRef'],ding['GPS GPSLatitudeRef']

        # a= 'GPS GPSLongitudeRef',ding['GPS GPSLongitudeRef']
        
        
            #  GPS['GPSLatitudeRef'] = str(value)
             

        # for din, value in ding.items():

            # print(din,value)
            # if re.match('GPS GPSLatitudeRef', din):
            #     # 纬度
            #     GPS['GPSLatitude'] = str(value)
            # elif re.match('GPS GPSLongitudeRef', din):
            #     # 经度
            #     GPS['GPSLongitudeRef'] = str(value)
            # elif re.match('GPS GPSAltitudeRef', din):
            #     # 海拔高度
            #     GPS['GPSAltitudeRef'] = str(value)   for din,value in ding.items():
           

if __name__ == '__main__':
    find_GPS_image('D:/pics/din1.jpg')
    