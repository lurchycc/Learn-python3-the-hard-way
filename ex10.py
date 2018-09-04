#转义字符的使用
tabby_cat="\tI'm tabbed in."
persian_cat="I'm spilt\na linr."
backslash_cat="I'm \\a \\ cat."

fat_cat="""
I'll do a list:
\t* Cat food
\t*Fishies
\t*Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
#\t表示句首空出四个空格
#\n表示换行