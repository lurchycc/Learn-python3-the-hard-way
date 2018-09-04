from sys import argv#导入模块

scipt,filename=argv#argv的用法

txt=open(filename)#使用open函数打开一个文件，open函数接受括号里的参数，然后赋给txt这个变量，txt返回的不是文件的内容而是一个文件对象
print(f"Here is the {filename}") 
print(txt.read())#对txt变量调用read函数
txt.close()
print("Type the filename again:")#input的方法打开文件
file_name=input()

txt_again=open(file_name)
print("look! print again!")
print(txt_again.read())
txt_again.close()
#打开一个txt文件！！？？