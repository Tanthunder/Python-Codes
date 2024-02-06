# Palindrome string 
#using slicing
'''def palindrome(input):
    temp = input[::-1]
    if temp == input:
        return 'Palindrome'
    else :
        return 'Not Palindrome'

input = input("Enter input")
x= palindrome(input)
print(x)'''

#using for loop
"""def palindrome(input):
    
    for i in range(len(input)):
        if input[i] != input[len(input)-i-1]:
            return('not palindrome')

    return('palindrome')

input = input("Enter input")
x= palindrome(input)
print(x)
"""
#using reversed and join function
#reversed returns object..so we can iterate over it

# Palindrome number
#using slice ...convert int into str ....not prefffered method
#using wwhile loop
'''def palindrome(input):
    temp = input
    value = 0
    while(temp>0):
        x = temp%10  #3 2
        value = value*10 + x #3 
        temp = temp//10 #12
    if input == value:
        return 'palindrome'
    else :
        return 'not palindrome'

input = int(input("Enter input"))
x= palindrome(input)
print(x)'''

#fibonacci series 0 1 1 2 3 5 8
#iteration using while and without using third variable

'''def fibonnaci(n):
    a=0
    b=1
    print(a)
    while(b<n):
        print(b)
        a,b= b, a+b
fibonnaci(6)'''

# using recursion
'''def fibonnaci(n):
    if n<=1:
        return n
    else:
        return(fibonnaci(n-1)+fibonnaci(n-2))

n = 4
if n <= 0 :
    print ('invalid')
else :
    for i in range(n):
        print(fibonnaci(i))'''

#similar logic can be used to find factorial using recursion
'''def factorial(n):
    if n <0:
        return 'invalid'
    elif (n == 1) or (n==0):
        return 1
    else:
        return(n*factorial(n-1))

print(factorial(-9))'''

# compress string 
#input aabbccc
# output a2b2c3
# using for loop
'''def comp(s):
    l= len(s)
    count = 1
    new_str=''
    
    for i in range(l-1):
        if s[i]==s[i+1]:
            count+=1

        else :
            new_str = new_str + s[i] + str(count)
            count = 1
    new_str = new_str + s[i] + str(count)
    return new_str
s = 'aabbccc'
print(comp(s))'''
#using while --use 2 while loops

# fizz buzz--if divisbale by 3 -- fizz ...if by 5 --buzz ...if by both or 15 -- fizbuzz..for other --number itself
'''def test(n):
    for i in range(n+1):
        if i%15 ==0:
            print ('fizbuzz')
        elif i%3 ==0:
            print( 'fizz')
        elif i%5 ==0:
            print('buzz')
        else :
            print(i)
test(20)'''
#using dict
'''def fizzbuzz(n):
    dict={3:'Fizz',5:'Buzz'}
    
    for i in range(1,n+1):
        res = ''
        for k,v in dict.items():
            if i%k == 0:
                res = res+v
        if not res:
            res= i
        print (res)
fizzbuzz(15)'''

#count of characters
# least occurring character

'''def least(s):
    ch = {}
    for i in s:
        if i in ch:
            ch[i]=ch[i]+1
        else:
            ch[i]=1
    print(ch)
    print(min(ch,key=ch.get))
least('abbccc')'''
#using inbuilt counter function
'''from collections import Counter
def count(s):
    res = Counter(s)
    print(res)
    print(min(res,key=res.get))

count('abbccc')'''

# count of specific element
# using built in count function
'''s='ghdhh'
res=s.count('h')'''
#without using count function
#use above logic for least occurrence and pass extra arguent in function...find value for that argument from list

#count all occurrences --use above logic for least occurrence till print(ch)

# to check if given number is prime or not
'''def prime(n):
    flag = False
    for i in range(2,((n//2)+1)):
        if n%i==0:
            flag = True
            break
    if flag == True:
        print('Prime')
    else :
        print('not prime')
prime(2)'''

#using for else loop....else part executes only if for compltely iterates without breaking...good approach

# display all prime numbers for particular range

def prime(st,end):
    for i in range(st,end+1):
        for j in range(2,i//2+1):
            if i%j ==0:
             break
        else:
          print(i)

prime(3,20)

#string modification
#input : Good_Morning
#output : gOOD.mORNING

'''def func(s):
    temp = s.split('_')
    print(temp)
    list=[]
    for i in temp:
        list.append(i[0].lower()+i[1:].upper())
    print(list)
    res= '.'.join(list)
    print(res)

func('Good_Morning')'''

#same can be achieved using string ... instead of append use + ....and for last extra dot use [:-1]

'''def func(l):
    if l[0]>l[1]:
        first=l[0]
        second= l[1]
    else:
        first=l[1]
        second= l[0]
    for i in range(2,len(l)):
        if l[i]>first:
            second= first
            first=l[i]
            
        elif l[i]>second and l[i]!=first :
            second=l[i]
    return second

print(func([2,4,6,56,44,3,4]))'''

# can also be slved using set(), sort and slice...but not recommended

#armstrong number--sum of cube of individual digits of number is equal to to number...153=1^3+5^3+3^3=153

'''def armstrong(n):
    sum = 0
    temp = n
    while(temp>0):
        x = temp%10
        sum = sum + x**3
        temp= temp//10
    if sum ==n:
        print('Yes')
    else:
        print('no')
armstrong(153)'''

#armstrong numbers in range ...add for loop above while loop to iterate over range

#Factorial
'''def facto(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact'''

#print(facto(5))

#sum of factorial of digits equal to number itself
'''def sum_fact(s):
    sum=0
    temp=s
    while (temp>0):
        digit = temp%10
        x=facto(digit)
        sum = sum + x
        temp=temp//10
    
    if sum==s:
        print('yess')
    else:
        print('no')

sum_fact(14)'''

#check above condition for all numbers in given range

'''def sum_fact(start,end):
    for i in range(start,end):
        sum=0
        temp=i
        while (temp>0):
          digit = temp%10
          x=facto(digit)
          sum = sum + x
          temp=temp//10
    
        if sum==i:
          print(i)

sum_fact(1,200000)'''

# dict comprehension to create dict {1:False,2:True,3:False...upto 10}

'''dict = {i:(True if i%2==0 else False) for i in range(1,11)}
print(dict)'''

# to chek if string is balanced or not(if have proper opening and closing brackets)
'''def balance(s):
    l1=['{','[','(']
    l2=['}',']',')']
    stack = []

    for i in s:
        if i in l1:
            stack.append(i)
        elif i in l2:
            pos= l2.index(i)
            temp = l1[pos]
            if temp == stack[len(stack)-1]:
                stack.pop()

            else :
                return 'unbalanced'
        if len(stack)==0:
            return 'balanced'

print(balance('{{}}'))'''

#take input having elements separated by , and positive int separated by ; 
#reverse parts of string of size of positive int and keep extra part as it is and print op
#asked in JP Morgan
'''
#ip=[1,2,3,4,5;2]
#op=[2,1,4,3,5]

#accept input as a list having elements separated by , and having positive int separated by ;
#separate ip into list and positive int
ip = input("Enter\n")
x1=ip[1:len(ip)-1]
a1=x1.split(';')
ip1=a1[0].split(',')
pint=int(a1[1])

#find number of parts and remaining elements of list
parts=len(ip1)//pint
extra=ip1[parts*pint:]

#logic to generate op
temp=[]
start,end=0,pint
for i in range(parts):
    torev= ip1[start:end]
    torev.reverse()
    temp.extend(torev)
    start=start+end
    end=end+pint

temp.extend(extra)
print(temp)
'''


#Find the longest common prefix string amongst an array of strings
# str1 = ["flower","flow","flight"]
# op = "fl"
# str2 = ["abc","pqr","xyz"]
# op = ""
"""words = ["abc","pqr","xyz"]
prefix = words[0]
for word in words[1:]:
   count = 0
   for i in range(len(prefix)):
      if (i < len(word)) and (i < len(prefix)) and (word[i] == prefix[i]):
         count+=1
      else:
          break
   prefix = prefix[:count]
print(prefix)"""

"""
Write sql query to get epmloyee having higher salay than his manager.
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+

select emp1.name from employee as emp1 
join employee as emp2 on emp1.manid = emp2.id 
where emp2.salary < emp1.salary
"""


"""
def visible_buildings(matrix):
    if not matrix:
        return 0

    n = len(matrix)
    count = n  # Counting the first building of each row which is always visible
    max_heights = [matrix[i][0] for i in range(n)]
    print(max_heights)
    zeros = 0
    for i in max_heights:
        if i == 0:
            zeros+=1

    for j in range(1, n):  # Iterate through each column
        max_height = matrix[0][j]
        for i in range(1, n):  # Iterate through each row in the column
            if matrix[i][j] > max_heights[j]:
                count += 1
                max_heights[j] = matrix[i][j]
                
    return count-zeros



# Example usage:
if __name__ == "__main__":
    s = "3 0 0 2 2 0 1 2 1 0 3 4 0 0 0 2"
    elements = list(map(int, s.strip().split()))
    n = int(len(elements) ** 0.5)  # Calculate the size of the square matrix
    matrix = [elements[i:i+n] for i in range(0, len(elements), n)]
    print(matrix)
    visible_count = visible_buildings(matrix)
    print("Number of visible buildings from the front:", visible_count)

"""