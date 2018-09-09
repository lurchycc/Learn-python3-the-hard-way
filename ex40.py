#import mystuff
#mystuff.apple()
#print(mystuff.varible)
#mystuff={"apple":"I am apple"}
#print(mystuff["apple"])
class Mysuff(object):#c创建一个叫Mystuff的类，他是object的一种

    def __init__(self):#类Mystuff有一个__init__，它接收self作为参数
        self.variable="this is the var."
    def apple(self):#类有一个名为Apple的函数。他接受self作为参数
        print("I am apple.")
thing=Mysuff()#将thing设置为类Mystuff的一个实例
thing.apple()#从thing里面找到apple函数，并使用self调用它
Q=thing.variable#从thing里面获取variable属性，并将其设置成Q（通常是个变量）
print(Q)
class Song(object):#创建一个叫Song的类，他是object的一种

    def __init__(self,lyrics,words):#类Song有一个__init__。他接收self，lyrics，words作为参数
        self.lyrics=lyrics
        self.words=words
    def song_me_a_song(self,wcc):#类Song有一个名叫song_me_a_song的函数，他接收self,wcc作为参数
        for line in wcc:
            print(line)
        for word in self.words:
            print(word)
happy_baby=Song(["I love you","and I miss you."],['666'])#将happy_babay设置为类Song的一个实例
#bulls_on_parade = Song(["fuck it!"],["666"])
happy_baby.song_me_a_song("123456")#在Song中找到song_me_a_song函数，并使用self和“123456”调用它
#bulls_on_parade.song_me_a_song()
#test_song=Song()
#test_song.song_me_a_song("123456")