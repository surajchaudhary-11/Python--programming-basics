# i =  1
# while i <=5:
#     print(i)
#     i += 1

# while-else
# n = 3
# while n>0:
#     print(n)
#     n -= 1
# else:
#     print('done')        



# print table 
# table =  int(input("enter the table number: "))
# i = 1
# while (i <= 10):
#     print(f" {i} * {table}  = {i*table} ")
#     i += 1


# sum of a digit  of a number
# n = int(input("enter the number: "))
# last_digit = 1
# total = 0
# while(n>0):
#     last_digit = n % 10 
#     total += last_digit
#     n = n//10

# print("sum of digits : ",total)    
    

# reverse a number

n =  int(input("enter a number: "))
reverse = 0

while n > 0:
    last_digit  = n % 10
    reverse = reverse * 10 + last_digit
    n =  n // 10
print("rreversed number: ",reverse)    