# a : 배열
# n : 배열의 길이
# key : 찾고자 하는 수
def seqSearch(a,n,key):
    i = 0
    while i<n and a[i] != key:
        i += 1
    if i < n: return i
    else: return -1


arr = [4,9,11,23,2,19,7]
print(seqSearch(arr,len(arr),2))
print(seqSearch(arr,len(arr),55555))



def seqSearch2(a,n,key):
    i = 0
    while i<n and a[i]<key:
        i += 1
    if i < n and a[i]==key: return i
    else: return -1

arrr = [1,2,3,4,5,6,7]
print(seqSearch2(arrr,7,2))
print(seqSearch2(arrr,7,8))

