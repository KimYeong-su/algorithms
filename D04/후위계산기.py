'''
6528-*2/+
-9.0

1. 피연산자를 만나면 스택에 push
2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산, 연산결과를 스택에 push
3. 수식이 끝나면 마지막으로 스택을 pop해서 출력
'''
def is_number(token):
    if token in ('*','/','-','+','(',')'):
        return False
    return True
def cal(token,a,b):
    if token == '+':
        return a+b
    elif token == '-':
        return a-b
    elif token == '*':
        return a*b
    elif token == '/':
        return a/b

postfix = list(input())
stack=[]

for c in postfix:
    if is_number(c):
        stack.append(c)
    else:
        b = float(stack.pop())
        a = float(stack.pop())
        stack.append(cal(c,a,b))

print(''.join(map(str,stack)))