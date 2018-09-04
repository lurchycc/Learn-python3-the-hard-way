from sys import argv#导入模块提前输入文件名

script,filename=argv

print(f"We're going to erase {filename}.")
print("If you don't want that,hit CTRL-C (^c).")
print("If you do want that hit RETURN.")

input("?")#输入选项  取消还是继续

print("Opening thr file...")
target = open(filename,'w')#以写的方式打开文件，赋给target这个文件对象（类似于DVD）

print("Truncating the file. Goodbye!")
target.truncate()#清空文件

print("Now I'm going to ask you for three lines.")

line1= input("line1:\n")#输入第一行内容
line2= input("line2:\n")
line3=input("linr3:\n")

print("I'm going to write these to thr file.")

target.write(f"{line1},{line2},{line3}")
#target.write(line1)#把line1内容写入到target这个文件对象里
#target.write("\n")#换行
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("And finally, we close it.")
target.close()#文件关闭
