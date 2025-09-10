# def comparecont(s:str,d:str)->str:
#     if(len(s)!=len(d)): return "No"
#     else:
#         for i in range(len(s)):
#             if s[i]!=d[i]:
#                 return "No"
#     return "Yes"
# s=input("Enter any string")
# d=input("Enter another string")
# print(f"{comparecont(s,d)}")

## count of specialcharcters,digits and aplhabets
# def compare(s):
#     a=0
#     d=0
#     sp=0
#     for i in s:
#         if i.isalpha():
#             a+=1
#         elif i.isdigit():
#             d+=1
#         else:
#             sp+=1
#     return [a,d,sp]
# s=input("Enter a String")
# print(f"The total count of alphabet,digit and special character {compare(s)}")

# #counting of vowels and consonents
# def counts(s:str)->list:
#     v=0
#     c=0
#     vowels="aeiou"
#     for i in s.lower():
#         if i.isalpha() and i in vowels:
#             v+=1
#         else:
#             c+=1
#     return [v,c]
# s=input("Enter a String")
# print(f"The count of vowels and consonents are {counts(s)}")

# #words in a string
# def counts(s:str)->int:
#     c=0
#     for i in s.split(" "):
#         c+=1
#     return c
# s=input("Enter a string separate by space")
# print(f"Total no of words are :{counts(s)}")

# #Frequency of charcters
# def count(s:str)->dict:
#     dict1={}
#     for i in s:
#         if i not in dict1:
#             dict1[i]=1
#         else:
#             dict1[i]+=1
#     return dict1
# s=input("Enter any String ")
# dict2=count(s)
# res=""
# for key,value in dict2.items():
#     res+=key+str(value)
# print(res)

# #Highest and lowest
# def high(s:str)->str:
#     max=0
#     name=""
#     dict1={}
#     for i in s:
#         if i not in dict1:
#             dict1[i]=1
#         else:
#             dict1[i]+=1
#     for key,value in dict1.items():
#         if max<value:
#             max=value
#             name=key
#     return name
# def low(s:str)->str:
#     max=float("inf")
#     name=""
#     dict1={}
#     for i in s:
#         if i not in dict1:
#             dict1[i]=1
#         else:
#             dict1[i]+=1
#     for key,value in dict1.items():
#         if max>value:
#             max=value
#             name=key
#     return name
# s=input("Enter any String ")
# print(f"{high(s)} has highest Frequency and {low(s)} has lowest frequency")
 