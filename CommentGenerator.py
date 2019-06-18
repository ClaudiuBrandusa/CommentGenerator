def CommentGenerator(Symbol,Text,MaxLength=119):
    if len(Symbol)>1:
        return "Your symbol should be just a character"
    if len(Text)==0:
        return 'Your text should have at least one character'
    if MaxLength < len(Text):
        return 'Your text is too long or your max length is too short'
    s='#'
    firstPart=0
    secondPart=0
    length=MaxLength-len(Text)
    if len(Text)%2==0:
        firstPart=length//2
        secondPart = firstPart+1
    else:
        firstPart=length//2
        secondPart=firstPart
    for i in range(firstPart):
        s+=Symbol
    for i in range(len(text)):
        if text[i]==' ':
            s+=symbol
        else:
            s+=text[i]
    for i in range(secondPart):
        s+=Symbol
    return s

#======================================================Application======================================================

symbol=input("Introduce the background symbol (just a character)")
text=input("Introduce the text, make sure that the text is not bigger than the MaxLength")
try:
    maxLength=int(input("Introduce the max length, leave it blank if you want to use the basic max length (119)"))
except:
    print(CommentGenerator(symbol, text))
else:
    print(CommentGenerator(symbol, text, maxLength))