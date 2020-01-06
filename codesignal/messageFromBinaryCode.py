def messageFromBinaryCode(code):
    return helper(code,"")
def helper(code,a):
    a += chr(int(code[:8],2))
    code = code[8:]
    if code:
        return helper(code,a)
    return a
