T = int(input())

for tc in range(1,T+1):
    t, N = input().split()
    N = int(N)

    num = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    counts = [0 for i in range(10)]
    arr = input().split()

    for i in range(len(arr)):
        for j in range(len(nums)):
            if arr[i] == num[j]:
                counts[j] += 1

    print(t)
    for i in range(len(counts)):
        for j in range(counts[i]):
            print(nums[i], end=" ")
    print()