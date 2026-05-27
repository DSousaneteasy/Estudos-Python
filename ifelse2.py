one = int(input("type a number between 1 and 10:"))
two = int(input("type a number betwenn 1 and 10:"))

if(one>=1) and (one <=10):
    if (two>=1) and(two<=10):
        print("your secret number is ", one*two)
    else:
        print("Incorrect second value!")
else:
    print("incorrect first value!")
