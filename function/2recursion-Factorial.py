#递归
#求n的阶乘

from itertools import product

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

def main():
    n=int(input("输入<=20的一个正整数："))
    if n>20:
        print("n的值不符合要求")
        exit()
    else:
        print("n的值为")
        print(factorial(n))

if __name__ == "__main__":
    main()