value=input("Type less than 6 characters:")
LetterNum=1

for Letter in value:
    print("Letter", LetterNum, "is", Letter)
    LetterNum+=1
    if LetterNum>6:
        print("The String is too long!")
        break
