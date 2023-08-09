# Problem: Remove x from string
def removeX(string,s): 
    pass
    if len(string)==0:
        return s
    if(string[0]!='x'):
        s+=string[0]

    return removeX(string[1:],s)


# Main
string = input()
s=""
print(removeX(string,s))

