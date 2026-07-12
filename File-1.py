# #traffic lights code
# # """light = input("Light is : ")
# # if(light == "red"):
# #     print("stop")
# # elif(light == "yellow"):
# #     print("look")
# # else:
# #     print("go")"""
# #sum
# # num1 = int(input("number 1 :"))
# # num2 = int(input("number 2 :"))
# # sum = num1+num2
# # print("sum is : " , sum)

# #area of square
# # side = int(input("enter side :"))
# # area = side*side
# # print("Side is :", area)

# # num1= float(input("Enter n1 :"))
# # num2= float(input("Enter n2 :"))
# # avg = (num1+num2)/2
# # print("Avg is : ", avg)

# # num1 = int(input("number 1 :"))
# # num2 = int(input("number 2 :"))
# # print(num1>=num2)
# # name = input("enter name :")

# # print("Dollar count is : ",name.count("$"))

# # m = int(input("Enter marks : "))
# # if(m>=90):
# #     print("Grade A")
# # elif(m < 90 and m >= 80):
# #     print("Grade B")
# # elif(m < 80 and m >= 70):
# #     print("Grade C")
# # else:
# #     print("Grade D")

# # num1 = int(input("number 1 :"))
# # if (num1%2 == 0):
# #     print("Even")
# # else: 
# #       print("Odd")

# # num1 = int(input("number 1 :"))
# # num2 = int(input("number 2 :"))
# # num3 = int(input("number 3 :"))
# # if (num1 > num2 and num1 > num3):
# #     print("num1 is greatest")
# # elif (num2 > num1 and num2 > num3):
# #     print("num2 is greatest")
# # else:
# #     print("num3 is greatest")
# # print("Enter 3 fav movies: ")
# # mov = []
# # m1 = input("")
# # m2 = input("")
# # m3 = input("")
# # mov.append(m1)
# # mov.append(m2)
# # mov.append(m3)
# # print(mov)

# # list = [1,2,1]
# # li = list.copy()
# # lirev = li.reverse()
# # if(lirev == list):
# #     print("palindrome")
# # else:
# #     print("not")

# # t1= ["C","D","A","A","B","B","A"]
# # cc=t1.count("A")
# # print("The count is : ",cc)

# # t1.sort()
# # print(t1)


# # info = {
# #     "table" : ["a piece of furniture","list of facts & figures"],
# #     "cat" : ["a small animal"]
# # }

# # print(info)

# # cla = {"py","ja","c++","py","jas","ja","py","ja","c++","c"}
# # print(cla)
# # print(len(cla))

# # marks = {}
# # x = int(input("Enter eng marks : "))
# # y = int(input("Enter phy marks : "))
# # z = int(input("Enter chm marks : "))

# # marks.update({"eng": x})
# # marks.update({"phy": y})
# # marks.update({"chm": z})
# # print(marks)


# # val = {9,"9.0"}
# # print(val)
# # n = 1
# # while n < 101 :
# #     print(n)
# #     n+=1
# # print("Loop end")

# # n = 100
# # while n >= 1 :
# #     print(n)
# #     n-= 1

# # n = int(input("Enter the number you want table for : "))
# # i = 1
# # while i <=10 :
# #     print(n, "*",i,"=",n*i)
# #     i += 1

# # group = [1,4,9,16,25,36,49,64,81,100]
# # g1 = []
# # n=1
# # while n<=10 :
# #     q = int(input("Enter element : "))
# #     g1.insert(n,q)
# #     n +=1

# # print(g1)


# # group = [1,4,9,16,25,36,49,64,81,100]
# # x = int(input("Enter x : "))
# # i = 0
# # found = False
# # while i < len(group) :
# #     if (x == group[i]):
# #         print("valid")
# #         found = True
# #         break
# #     i += 1
# # if (found == False):
# #     print("invalid")

# #group = [1,4,9,16,25,36,49,64,81,100]
# # for val in group :
# #     print(val)

# # group = [1,4,9,16,25,36,49,64,81,100]
# # x=64
# # for val in group :
# #     if (val == x):
# #      print("val found ")
# #      break
# # else :
# #     print("finding")

# # for el in range(101):
# #     print(el)

# # for el in range(100,0,-1):
# #     print(el)
# # n=int(input("Enter the number whose table is  required : "))

# # for i in range(1,11):
# #     print(n*i)


# # n = int(input("Enter the num till sum is reqd :"))
# # i=1
# # sum=0
# # while (i<=n):
# #     sum = sum +i
# #     i += 1

# # print("The sum is : ",sum)

# # n = int(input("Enter the num till fact is reqd :"))
# # fact=1
# # for i in range(1,n+1) :
# #     fact*=i
# # print("Fact is : ",fact)

# # def avg_no(a,b,c):
# #     avg = (a+b+c)/3
# #     print(avg)
# # avg_no(1,2,3)

# # def list_len(list1):
# #     return len(list1)
# # ab = [1,2,3,4,5,6]
# # print(list_len(ab))

# # ab = [1,2,3,4]
# # def print_ele(li):
# #     for item in li:
# #         print(item,end = " ")

# # print_ele(ab)


# # def fact(n):
# #     fa = 1
# #     for items in range(1,n+1):
# #         fa *= items
# #     print(fa)

# # fact(5)
# # def converter(usd_val):
# #     inr = usd_val* 100
# #     print(usd_val,"USD=",inr,"INR")
# # converter(100)

# # def sum(n):
# #     if (n == 0): 
# #         return 0
# #     return sum(n-1) + n
# # su = sum(10)   
# # print(su)

# # ab = [1,2,3,4,5]
# # def print_ele(li,idx=0):
# #     if (idx == len(li)):
# #         return
# #     print(li[idx])
# #     print_ele(li,idx+1)

# # print_ele(ab)

# # class Student:
# #     college_name = "ABC College"
# #     def __init__(self,name,marks):
# #         self.name = name
# #         self.marks = marks
# #     def wlm(self):
# #         print("welcome Student",self.name)
# #     def st_marks(self):
# #         return self.marks
# #     def get_avg(self):
# #         sum = 0
# #         for val in self.marks:
# #             sum += val
# #         print("AVG is ",sum/3)
# # s1 = Student("Abhishek",[99,98,97])
# # s1.wlm()
# # print(s1.st_marks())
# # s1.get_avg()

# # class Accounts:
# #     def __init__(self,acc_no,balance):
# #         self.acc_no = acc_no
# #         self.balance = balance
# #     def cred(self, amt):
# #         self.balance += amt
# #         print("Rs.",amt,"was credited")
# #         print("Available balance : ", self.balance)       
# #     def debt(self, amt):
# #         self.balance -= amt
# #         print("Rs.",amt,"was debited")
# #         print("Available balance : ", self.balance)
# # s1 = Accounts(123,1200)
# # print("Account no : ",s1.acc_no)
# # print("Current balance :",s1.balance)
# # s1.cred(1200)
# # s1.debt(1200)
# # class Circl:
# #     def __init__(self,radius):
# #         self.radius = radius 
# #     def area(self):
# #         return 3.14 * self.radius * self.radius
# #     def perimeter(self):
# #         return 2 * 3.14 * self.radius
# # c1 = Circl(21)
# # print(c1.area())
# # print(c1.perimeter())

# # class Employee:
# #     def __init__(self,role,depart,sal):
# #         self.role = role
# #         self.depart = depart
# #         self.sal = sal
# #     def ShowDetails(self):
# #         print("role : " ,self.role)
# #         print("Department : " ,self.depart)
# #         print("salary : " ,self.sal)
# # class Engineer(Employee):
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #         super().__init__("Engineer","IT",200000)
# #     def showInfo(self):
# #         print("name : ",self.name)
# #         print("age : ",self.age)

# # E1 = Engineer("Abhishek","19")
# # E1.ShowDetails()
# # E1.showInfo()

# # class Order:
# #     def __init__(self,item,price):
# #         self.item = item 
# #         self.price = price
# #     def __gt__(self,ord2):
# #         return self.price > ord2.price
    
# # ord1 = Order("chips",20)
# # ord2 = Order("tea",15)
# # print(ord1 > ord2)


# # #Mini Project-1
# # import random
# # target = random.randint(1,100)
# # while True:
# #     userChoice = input("Guess the target or Quiet(Q):")
# #     if(userChoice == "Q"):
# #         break
# #     userChoice = int(userChoice)
# #     if(userChoice == target):
# #         print("Correct Guess !!")
# #         break
# #     elif(userChoice < target):
# #         print("take a bigger guess")
# #     else:
# #         print("Take a smaller Guess")
# # print("---GAME OVER---")
 

# # #Mini Project -2
# # import random as r
# # import string as s
# # charValues = s.ascii_letters + s.digits + s.punctuation
# # pass_len = 4
# # password = ""
# # for i in range(pass_len):
# #     password += r.choice(charValues)
# # print("Your random pass is :",password)f




# #Functions in python
# # def sum(li):
# #     sum = 0
# #     for i in li:
# #         sum += i
# #     return sum
# # lis = [1,2,3,4]
# # print(sum(lis))

# # li = [1,2,3,4]
# # def rev(li):
# #     st=0
# #     end=len(li)-1
# #     while st<end:
# #         li[st] = li[end]
# #         st+=1
# #         end-=1
# #     return li
# # rev(print(li))
# # li = [1, 2, 3, 4]

# # def rev(li):
# #     st = 0
# #     end = len(li) - 1

# #     while st < end:
# #         li[st], li[end] = li[end], li[st]
# #         st += 1
# #         end -= 1

# #     return li

# # print(rev(li))
# # a = [1,2,3]
# # b = a
# # b += [4]
# # print(a)

# # li = [1,2,9999,-4]
# # def High(lis):
# #     max = li[0]
# #     for i in li:
# #         if max < i :
# #             max = i
# #     return max
# # print(High(li))
# # def Min(lis):
# #     min = li[0]
# #     for i in li:
# #         if min>i:
# #             min=i
# #     return min
# # print(Min(li))



# # f = open("files.txt","x")
# # print("Created file successfully")
# # f.close()
# # f = open("files.txt","w")
# # f.write("My name is Abdul\n")
# # f.write("I am from Abdullapur\n")
# # f.write("My age is 99\n")
# # # f.close()
# # f = open("files.txt", "r")
# # print(f.readline())
# # print(f.readline())
# # f.close()
# count = 0
# with open("files.txt", "r") as f:
#     for line in f:
#         for ch in line:
#             if ch.isalpha():
#                 count += 1

# print(count)
# with open('file.txt','r') as f:
#     print(f.read())

# with open("files.txt","w") as f1:
#     f1.write("Abhi123 1234")


# username=input("Username - ")
# password=input("Password - ")
# with open("files.txt","r") as f:
#      x=f.read()
#      if username in x and password in x:
#           print("login successfuly")
                
#      else:
#           print("invalid credential")

