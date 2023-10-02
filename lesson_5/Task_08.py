def my_round(number,count):
    if ((number * 10**(count + 1))%10 >= 5):
        answer = int(number * 10**count)/10**count
        return (answer + 0.1**count)
    else:
        answer = int(number * 10 ** count )/ 10 ** count
        return(answer)


print(my_round(4.345956,3))
