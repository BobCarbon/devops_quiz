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
    # Run minor error handling
    try:
        n = int(n)
    except ValueError:
        print('Please input a number - terminating script.')
        quit()

    if n == 0:
        return 'uncle'

    # Use mod to check division by 3
    is_aunty = (n % 3) == 0

    if is_aunty:
        return 'aunty'

    return 'uncle'