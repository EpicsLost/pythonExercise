
import os,sys
print(dir())
print(__file__)
print(os.path.abspath(__file__))#获得绝对路径（终端中）
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)

print(sys.path)
print(sys.argv)