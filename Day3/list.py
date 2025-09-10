# n=int(input(("Enter the size of a list")))
# lt=[]
# for i in range(n):
#     lt.append(int(input(f"Enter the {i} element ")))
# print(lt)

# lt=[-1,0,23,-98,-67,100,76]
# ltn=[]
# for i in range(len(lt)):
#     if(lt[i]<0):
#         ltn.append(lt[i])
# print(f"The negative elements are :{ltn}")

#Second max
# lt = [12, 23, 34, 56, 67, 78, 89, 90]

# max1 = max2 = float('-inf')  # initialize to negative infinity

# for num in lt:
#     if num > max1:
#         max2 = max1   # update second max
#         max1 = num    # update max
#     elif num > max2 and num != max1:
#         max2 = num

# print("Maximum:", max1)
# print("Second Maximum:", max2)

# lt=[1,2,3,4,5,0]
# o=0
# e=0
# for num in lt:
#     if(num&1==0 and num!=0):
#         e+=1
#     elif(num!=0 and num&1==1):
#         o+=1
# print(f"{o} odd {e} even")

# lt=[1,2,3,4,5,6,7,89]
# pos=int(input("Enter the position of an element to delete "))
# if pos>=len(lt):
#     print("Index out of Bounds")
# else:
#     lt.pop(pos)
#     print(lt)

#Frequency
# lt=[1,1,2,3,4,5,5,3,4,5,7,8,7,7,7,8,8]
# dict1={}
# for num in lt:
#     if num in dict1.keys():
#         dict1[num]+=1
#     else:
#         dict1[num]=1

# for key,value in dict1.items():
#     print(f"{key}->{value}")


#unique elements
# lt=[1,1,2,3,4,5,5,3,4,5,7,8,7,7,7,8,8]
# ltn=[]
# for num in lt:
#     if num not in ltn:
#         ltn.append(num)
# print(ltn)
#Second way to do unique
# lt=[1,1,2,3,4,5,5,3,4,5,7,8,7,7,7,8,8]
# print(set(lt))


#duplicates count
# def duplicate(li:list)-> int:
#     return len(li)-len(set(li))
# li=[1,1,1,1,2,2,2,3,3,3,4,4,45,5,5]
# print(duplicate(li))