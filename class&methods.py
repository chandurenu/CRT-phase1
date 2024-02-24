#write a python program to print the factorial of a given number using class and methods
class day6:
    def fact(self,n):
        f=1
        for i in range(1,n+1):
            f*=i
        print(f)
obj=day6()
obj.fact(int(input()))
