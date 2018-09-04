def break_words(stuff):
    """This function will break up words for us."""
    words= stuff.split(' ')#''引号之间的空格不能不写 他是分割句子的标志
    return words
def sort_words(words):
    """sorts the words"""
    return sorted(words)#打乱句子顺序
def print_first_word(words):
    """Prints the first word after popping it off."""
    word=words.pop(0)
    print(word)
def print_last_word(words):
    """Prins the last word after popping it off."""
    word=words.pop(-1)
    print(word)
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words= break_words(sentence)
    return sort_words(words)
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words=break_words(sentence)#恢复到原来的句子
    print_first_word(words)
    print_last_word(words)
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)