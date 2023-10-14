def input_list(prompt:"",set:" ",element_type: int):
    print(prompt)
    lst = list(map(lambda num: element_type(num), input().split(set)))

    print(lst)

input_list("Privet"," ",int)