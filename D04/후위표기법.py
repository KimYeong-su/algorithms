infix=list('(6+5*(2-8)/2)')
postfix = []
stack = []

def is_number(token):
    if token in ('*','/','-','+','(',')'):
        return False
    return True

def icp(token):
    if token == '*' or token == '/':
        return 2
    elif token == '+' or token == '-':
        return 1
    elif token == '(':
        return 3

def isp(token):
    if token == '*' or token == '/':
        return 2
    elif token == '+' or token == '-':
        return 1
    elif token == '(':
        return 0
top = -1
for t in infix:
    if is_number(t):
        postfix.append(t)
    else:
        if len(stack)==0:
            top +=1
            stack.append(t)
        else:
            if t == ')':
                while stack[top] != '(':
                    postfix.append(stack.pop())
                    top -= 1
                stack.pop()
                top -= 1
            elif (icp(t)>isp(stack[top])):
                stack.append(t)
                top +=1
            else:
                while icp(t)<=isp(stack[top]):
                    postfix.append(stack.pop())
                    top -=1
                stack.append(t)
                top +=1


print(''.join(postfix))
