import random
from urllib.request import urlopen
import sys
#导入模块
WORD_URL="http://learncodethehardway.org/words.txt"
WORDS =[]
#????这是一个网址
PHRASES = {
    "class %%%(%%%):":
        "make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self,***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self,@@@)":
        "class %%% has a function *** that takes self and @@@ params.",
    "***= %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self,@@@.",
    "***.***= '***'":
        "From *** get the *** attribute and set it to '***'."
}
#??????????????????????????????????????????????\这是一个字典
#do they want to drill phrases first
if len(sys.argv)== 2 and sys.argv[1] == "english":#如果命令行启动了两个参数而且第二个是english，则返回true，否则返回false
    PHRASE_FIRST=True
else:
    PHRASE_FIRST=False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))#从这个网址中读取字符加到WORDS中。word.strip()，用来去除头尾指定的字符默认是空格编码格式以utf-8

def convert(snippet,phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
    #???w.capitalize()是将w字符串的第一个字母大写
    #random.sample(list,5),表示从list里面有放回的随机抽取5个元素
    other_names=random.sample(WORDS,snippet.count("***"))
    #???
    results=[]
    param_names=[]
    for i in range(0,snippet.count("@@@")):
        param_count=random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS,param_count)))
    
    for sentence in snippet,phrase:
        result=sentence[:]

        #fake class names
        for word in class_names:
            result=result.replace("%%%",word,1)
        for word in other_names:
            result = result.replace("***",word,1)

        for word in param_names:
                result=result.replace("@@@",word,1)

        results.append(result)
    return results

    #keep going until they hit CTRL-D
try:
    while True:
        snippets=list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question,answer = convert(snippet,phrase)
            if PHRASE_FIRST:
                question,answer=answer,question
                
            print(question)

            input(">")
            print(f"ANSWER:{answer}\n\n")
except EOFError:
    print("\nBye")
        