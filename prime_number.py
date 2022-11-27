# Program to check if a number is prime or not


def prime_check(num):

# prime numbers are greater than 1
    if num > 1:

        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")

                break
        else:
            print(num,"is a prime number")


    else:
        print(num,"is not a prime number")

n = int(input("Plese enter the number: "))
prime_check(num = n)