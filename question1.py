#Write a program which take a number N as input from the user and You need to reverse the number.
#Code:
N=int(input("Enter the integer number"))
reverse_num=0
while(N>0):
    remainder=N%10
    reverse_num=(reverse_num*10)+remainder
    N=N//10
print("The reverse number is:{}".format(reverse_num))
