T = int(input())
for tc in range(1,T+1):
    s = list(input())
    while True:
        stack=[]
        for i in s:
            if len(stack)==0:
                stack.append(i)
            else:
                if stack[-1]==i:
                    stack.pop()
                else:
                    stack.append(i)
        if stack == s:
            break
        s = stack
    print('#{} {}'.format(tc,len(stack)))