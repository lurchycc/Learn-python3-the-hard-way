types_of_people=10#定义变量
x=f"There are {types_of_people} types of people."#格式化字符串把变量放入指定位置

binary="binary"
do_not="don't"
y=f"Those wwho know {binary} and those who {do_not}."#变量也可以是字符串 放入指定位置组成一句哈
#话

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said:'{y}'")

hilarious="False"
joke_evaluation = "Isn't that joke so funny?!{}"#使用{}预留一个位置

print(joke_evaluation.format(hilarious))#使用format将变量传入

w="This is the left side of..."
e="a string with a right side."

print(w+e)#“+”可以连接两个句子