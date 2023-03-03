# python docstrings are the string literals that appear right after the definition of a function, module, class .
def square(n):
    '''
    takes a number n and return its square
    '''
    return n*n


def sum(n1, n2):
    ans = n1 + n2
    '''
    takes two integer arguments and return sum
    '''
    return ans


val = square(5)
print(val)

print(square.__doc__)  # -> takes a number n and return its square
print(sum.__doc__)  # -> None

# docstrings are not ignored and doxtring change krne se programe ke output change ho skte hain lekin comment change krne se programme ke output change nhi ho skte
# docstring should be return just before the function body
