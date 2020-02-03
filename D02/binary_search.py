# 이진검색 -> 자료가 정렬 되어 있는 상태에서만 가능
'''
검색 시작점, 종료점을 설정함 ( 반복이 진행되면서 시작점, 종료점 갱신)
반복 시작
시작점이 종료점보다 커진다면 더이상 탐색 불가하므로 반복 종료
    중앙값을 구함
    중앙점의 값과 찾고자하는 값을 비교해봄
        같다면?        찾았으니까 True 리턴
        크면?          왼쪽 탐색 -> 종료점을 갱신
        작으면?        오른쪽 탐색 -> 시작점을 갱신
'''

def binary_search(a,n,key):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == key:
            return True
        elif key < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

arr = [2,4,7,9,11,19,23]
print(binary_search(arr,len(arr),7))
print(binary_search(arr,len(arr),20))