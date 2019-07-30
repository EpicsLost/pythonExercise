import shutil

f1 = open("time.py","r")
f2 = open("微信人数_new.py","w")

shutil.copyfileobj(f1,f2)