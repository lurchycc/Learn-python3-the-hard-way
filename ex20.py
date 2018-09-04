from sys import argv

script, input_file= argv

def print_all(f):#读取文件
    print(f.read())

def rewind(f):#设置文件读取指针位置
    f.seek(0)#设置指针到文件开头

def print_a_line(line_count,f):#
    print(line_count, f.readline(),end="")#读取文件的某一行
    
current_file=open(input_file)#打开文件

print("First let's print the whole file:\n")

print_all(current_file)#把文件所有内容打印出来

print("Now let's  rewind,kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line=1
print_a_line(current_line,current_file)#打印第一行

current_line+=1
print_a_line(current_line,current_file)#打印第一行的下一行

current_line+=1
print_a_line(current_line,current_file)#打印第一行下一行的下一行 