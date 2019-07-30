
def isValid(s):
    left = ["(","[","{"]
    right = [")","]","}"]

    stack = []
    for i in s:
        if i in left:
            stack.append(i)
        elif i in right:
            if not stack or left.index(stack.pop()) != right.index(i):
                return False

    return not stack


print(isValid("(["))
