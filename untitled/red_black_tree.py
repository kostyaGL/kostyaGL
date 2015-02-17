def checkio(text):
    curl, brackets, square = 0,0,0
    for i in text:
        if '{' in i:
            curl+=1
        elif '}' in i:
            curl-=1
        elif '[' in i:
            square+=1
        elif ']' in i:
            square-=1
        elif '(' in i:
            brackets+=1
        elif ')' in i:
            brackets-=1
    return curl, brackets, square
print checkio("{}[]()()(")