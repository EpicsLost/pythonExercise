import shelve

f = shelve.open("shelve")

d = {"name":"alex","age":"22"}
l = [1,2,3,4,"rain"]

f["names"] = d
f["info_dic"] = l

f.close()