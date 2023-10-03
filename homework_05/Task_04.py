def get_longest_word(sentence):
    list = sentence.split()
    words = 0
    for i in list:
        words +=1
    count = 0
    max = 0
    i_max = 0
    i = 0
    while words>i:
        for element in list[i]:
            count+=1
        if count > max:
            max = count
            i_max = i
        i+=1
        count = 0
    return(list[i_max])
print(get_longest_word("privet my name is maxim"))
