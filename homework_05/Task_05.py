def get_most_frequent_word(sentence):
    list = sentence.split()
    word = 0
    word_buf=0
    repeat = 0
    repeat_buf = 0
    for i in list:
        for a in list:
            if i == a:
                word_buf = i
                repeat_buf += 1
        if repeat_buf>repeat:
            repeat=repeat_buf
            word = word_buf
        repeat_buf = 0
    return(f'{word} repeates {repeat} times')

print(get_most_frequent_word("and and and for for for for for no no and"))