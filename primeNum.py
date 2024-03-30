# Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
# Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
def algorithm(n):
    prime_list = []
    for i in range(2,n+1):
        if i not in prime_list:
            print(i)
            for j in range(i*i,n+1,i):
                prime_list.append(j)
algorithm(5)