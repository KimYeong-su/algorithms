T = int(input())

for tc in range(1,T+1):
    s = input()
    result = 0
    stack = []
    for i in range(len(s)):
        if s[i] =='{':
            stack.append(s[i])
        elif s[i] == '(':
            stack.append(s[i])
        elif s[i] == '}':
            if len(stack)==0:
                break
            if stack[-1] != '{':
                break
            else:
                stack.pop()
        elif s[i] == ')':
            if len(stack)==0:
                break
            if stack[-1] != '(':
                break
            else:
                stack.pop()
        if i == len(s)-1 and len(stack)==0:
            result = 1
    print('#{} {}'.format(tc,result))