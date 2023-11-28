
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("Error: 没有找到文件或读取文件失败")
finally:
    print("关闭文件")
    fh.close()


with open("testfile", "w") as f:
    f.write("这是一个测试文件，用于测试异常!!")