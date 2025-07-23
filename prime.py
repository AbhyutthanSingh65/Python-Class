def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_digits = {2, 3, 5, 7}

print("the prime numvbers are:\n")
for num in range(100, 1000):  
    if is_prime(num):  
        digits = [int(d) for d in str(num)]
        digit_sum = sum(digits)
        if is_prime(digit_sum): 
            if all(d in prime_digits for d in digits):  
                print(num)
