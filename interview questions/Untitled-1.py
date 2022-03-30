# Que 1.

# strr = "I have 5 years of Exp and I am 25 years old. 123 1AB234"
# Output:
# 5
# 25
# 123

# # Que 1.
 
# s = "I have 5 years of Exp and I am 25 years old. 123 1AB234"
# # Output:
# # 5
# # 25
# # 123
# a=s.split(" ")
 
 
 
 
# for i in a:
 
#     if i.isnumeric():
#         print(i)



# Que 2.
# Input:  12, 10, 102, 31, 15
# Output: 10, 12, 102, 31, 15

 
# arr= 12, 10, 102, 31, 15
# # Output: 10, 12, 102, 31, 15
# n=len(arr)
 
# def summm(n):
#     sum__r=0
#     while n >0:
#         sum__r+=n%10
#         n=n//10
#     print(sum__r)
#     return sum__r
 
# def sort(arr,n):
 
#     reslist=[]
#     for i in range(n):
#         reslist.append([summm(arr[i]),arr[i]])
#     print(reslist)
#     reslist.sort()
#     for i in range(len(reslist)):
#         print(reslist[i][1],end=" ")
 
# sort(arr,n)


# Que 3.
# What will be the output of the following code chunk.
# def str_matcher(string):
#     print('Inside a string matcher')
#     print('String is '+ string)
    
# def list_matcher(lis):
#     print('Inside a list matcher')
#     print('list is '+ lis)
    
# def get_matcher(type_):
#     switcher = {'str': str_matcher, 'list': list_matcher}
#     return switcher[type_]

# matcher = get_matcher('str')
# matcher('Mayank')
# Ans: string is mayank


# Que 4.
#  def test(x, y, z):
#     print(x, y, z)

# testDict = {'x': 1, 'y': 2, 'z': 3} 
# test(*testDict)
# test(**testDict)

# Que 5.

# Table Student

# id		name		sub		marks
# 1		rahul		Sci		20
# 2		rahul		hindi		22
# 3		rahul		maths		21
# 4		Safiyat		sci		24
# 5		rahul		hist		19
# 6		amit		eng		25
# 7		Aakash	sci		18
# 8		amit		maths		17
# 9		amit		sci		23
# 10		amit		hist		22

# write a SQL query for selecting the second-highest marks in the table
# write SQL query for selecting the second-highest marks in sci
# SQL query for highest marks in sci, hist, maths

# Select  * from Student where marks in ( select marks from Student order by desc limit 1,1)





# Que 6 
# Tringle 

# Id 	A	B	C
# 1	2	3	4	
# 2	4	5	6	
# 3	5	5	5	
# 4	6	7	8	
# 5	7	7	7
# Select a. id from triangle a  innerjoin triangle b on a.id =b.id  where a.A=b.B  innerjoin triangle c on b.id =c.id where b.B=c.C;

# [5:12 PM] Mayank  Kumar (Guest)
#     {​​​​​​​​
#     "a1":"123",
#     "a2":"45",
#     "a3":"67",
#     "a4":{​​​​​​​​
#             "a1":"45",
#             "a5":{​​​​​​​​
#                     "a7":"20",
#                     "a4": [1,2,3,4,5,6],
#                     "a5":"13"
#                 }​​​​​​​​,
#             "a3":"56"
#         }​​​​​​​​
#     }​​​​​​​​
# ​[5:13 PM] Mayank  Kumar (Guest)
#     input: a1
# output: "a1":"123", "a1":"45"

# 1 2 3 4 5
# 3 4 5 8 10
# 3 5 7 9 11
# 1 3 5 7 9
# output: 3 5