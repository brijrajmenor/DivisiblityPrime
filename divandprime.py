num=int
def prime():
        num = int(input("Enter a number: "))
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    print(num,"is not a prime number")
                    break
                else:
                    print(num,"is a prime number")
        else:
            print(num,"is not a prime number")
def divisibility():
        num = int(input("Enter a number: "))
        divi=input("Enter the number with which you wanna check its divisibility: ")
        if int(num)%int(divi)==0:
            quo=int(num)/int(divi)
            int(quo)
            print (+num+" is divisible by " +divi+" and the quotient is "+str(quo))
        else:
            print(+num+ " is not divisible by "+divi)

ch=int(input("\n1. To check a number is prime or not\n2. Divisibility of a number with any given number\n3. Exit\nEnter your choice: "))
switcher = {
1: prime(),
2: divisibility(),
3:exit(1)
}