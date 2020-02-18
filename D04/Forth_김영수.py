T=int(input())
for tc in range(1,T+1):
    equation = list(map(str,input().split()))
    stack = []

    for s in equation:
        if s in ('+','-','*','/'):
            if len(stack)>1:
                b = int(stack.pop())
                a = int(stack.pop())
                if s == '+':
                    stack.append(a+b)
                elif s == '-':
                    stack.append(a-b)
                elif s == '/':
                    stack.append(a/b)
                else:
                    stack.append(a*b)
            else:
                print('#{} error'.format(tc))
                break
        elif s == '.':
            print('#{} {}'.format(tc,stack.pop()))
        else:
            stack.append(s)