#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)

def isPalindrome(n):
    temp = n
    reverse_number = 0
    result = False
    while n>0:
        rem = n%10
        reverse_number = reverse_number*10 + rem
        n //= 10
    if temp == reverse_number:
        result = True
    return result



def doublePalindrome(n):
    #checking less than n
    final_list = []
    for i in range(1,n):
        if isPalindrome(i) and isPalindrome(int(bin(i)[2:])):
            final_list.append(i)
    return sum(final_list)

final = doublePalindrome(1000000)
print(final)