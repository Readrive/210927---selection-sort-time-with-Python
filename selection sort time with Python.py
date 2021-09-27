import time
import random

#선택 정렬
def sel_sort(array):
    for i in range(len(array)):
        min_index = i # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i] # 스와프
    return array

def sel_sort(array_b):
    for i in range(len(array_b)):
        min_index = i # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(array_b)):
            if array_b[min_index] > array_b[j]:
                min_index = j
        array_b[i], array_b[min_index] = array_b[min_index], array_b[i] # 스와프
    return array_b

#array = [x for x in range(1001)]
#random.shuffle(array)


#최악
array_b = []
for i in range(10000, 1, -1):
    array_b.append(i)


#최선
array = []

for i in range(1, 10000):
    array.append(i)

start_time = time.time()
sel_sort(array_b) #선택정렬
end_time = time.time()
print("선택 정렬 최악 성능 측정:", end_time - start_time) # 수행 시간 출력

start_time = time.time()
sel_sort(array) #선택정렬
end_time = time.time()
print("선택 정렬 최선 성능 측정:", end_time - start_time) # 수행 시간 출력
