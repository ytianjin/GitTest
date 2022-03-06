
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
        # data =ding.setdefault('GPS GPSLongitude','it')   
        for din,value in ding.items():
            if re.match('GPS GPSLatitudeRef', din):
                GPS['GPSLatitudeRef'] = str(value)

            elif re.match('GPS GPSLongitudeRef', din):# 经度
                GPS['GPSLongitudeRef(经度)'] = str(value)

            elif re.match('GPS GPSAltitudeRef', din):# 海拔高度
                GPS['GPSAltitudeRef(海拔高度)'] = str(value)

            elif re.match('GPS GPSLatitude', din):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).group()
                    GPS['GPSLatitude(纬度)'] = int(match_result[0], int(match_result[1], int(match_result[2]/int(match_result[3]))))
                except:
                    GPS['GPSLatitudeRef(纬度)'] = str(value)
            elif re.match('GPS GPSLongitude', din):
                try:
                    match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
                    GPS['GPSLongitude(经度)'] = int(match_result[0]), int(match_result[1]), int(match_result[2]/int(match_result[3]))
                except:
                    GPS['GPSLongitude(经度)'] = str(value)
            elif re.match('GPS GPSAltitude', din):
                GPS['GPSAltitude(海拔高度)'] =str (value)
            elif re.match('Image DateTime', din):
                date = str(value)
    return {'GPS':GPS,'时间':date}

            # GPS['GPSLatitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
            # GPS['GPSLatitude'] = match_result
   
            


if __name__ == '__main__':
    GPS_info = find_GPS_image('D:/pics/din1.jpg')
    print(GPS_info)
