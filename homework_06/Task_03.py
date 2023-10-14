def remove_vowels(lst):
    return(list(filter(lambda letters: letters not in ['a','e','u','i','o', 'Y','A','E','U','I','O', 'Y'], lst)))
lst = input().split()
print(remove_vowels(lst))