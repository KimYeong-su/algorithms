'''
2
()()((()))
((()((((()()((()())((())))))
'''
T = int(input())
for tc in range(1,T+1):
    s = input()
    top = -1
    check_list = []
    for i in s:
        if i=='(':
            top+=1
            check_list.append(i)
        elif i==')':
            if len(check_list) != 0:
                a=check_list.pop(top)
                top -= 1
            else:
                check_list.append(i)
                break
    if len(check_list) == 0:
        print(1)
    else:
        print(0)

''' 
# solution
def find_match(): 
    s = list()
    for i in range(len(txt)):
        if txt[i] == '(':
            s.append(txt[i])
        elif txt[i]==')':
            if (len(s) == 0):
                return 0
            else:
                s.pop()
    if len(s) != 0:
        return 0
    else:
        return 1

T = int(input())
for tc in range(1,T+1):
    txt = input()
    print("#{} {}".format(tc, find_match()))
'''