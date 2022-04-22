# 将0x00～0xff写入二进制文件

with open('binfile.bin', 'bw') as f: # 二进制写入模式
    f.write(bytes(range(0, 256)))
