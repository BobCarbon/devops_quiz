"""
Using your preferred programming or scripting language, 
write a function that takes a number as an argument and
return the string 'aunty' if divisible by 3. Otherwise
it returns 'uncle'.
"""

def ommer(n):
    """
    If given n is divisible by 3, return string 'aunty'.
    Else, return string 'uncle'.
    """
    n = int(n)
    if n == 0:
        return 'uncle'

    is_aunty = (n % 3) == 0

    if is_aunty:
        return 'aunty'

    return 'uncle'

if __name__ == "__main__":
    number = 0
    print(ommer(number))