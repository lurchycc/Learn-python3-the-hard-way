from sys import argv
c=input("输入一个c：")
cc=input("please input double c:")
ccc=input("you konw what to input:")
script,c,cc,ccc=argv
print(c)
print(cc)
print(ccc)
#哈哈，终于搞懂了  argv就是提前输入，在程序执行之前就需要就要输入，argv是个列表。。。
#如果参数是在执行程序前就需要输入，可以用argv，在程序运行时需要输入数据可以用input