list1=[1,2,3,4]


print(list1[-1])

list2=[5,6,7,8]

list3 = list1+list2
print(list3)

list4=[list1]+[list2]

print(list4)

list2.append(9)

print(list2)


# 요소 제거
print("="*50)
arr=[1,2,3,4]
arr.remove(1)
print(arr)   #[5,6,7]

del arr[0]
print(arr)  #[6,7]

# 끝에 추가
print("="*50)
arr2=[5,6,7,8]
arr2.append(9)
print(arr2)


#원하는 위치에 추가 
print("="*50)
arr3=[5,6,7,8]
arr3.insert(2,500)
print(arr3)

#정렬
print("="*50)
arr4=[8,5,1,3]
arr4.sort()
print(arr4)
arr4.reverse           #뒤집는거 
print(arr4)


# 반복문
print("="*50)
arr5=[1,3,5,7]

for i in arr5:
       print(i)

print("="*50)

for i in range(0,6):      #끝에 있는 값 그 값 직전까지  range라는 함수 기억하기 
    print(i)
    print(33)
  
