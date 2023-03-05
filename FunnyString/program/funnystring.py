def FunnyString(s):
    x = []; y =[]
    for i in range(len(s)):
        x.append(abs(ord(s[i]) - ord(s[i-1])))
        y.append(abs(ord(s[-i]) - ord(s[-i-1])))
        
    if x == y: 
        return "Funny"
    return "Not Funny"