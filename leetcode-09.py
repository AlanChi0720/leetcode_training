def isPalidrome(x):
    if x < 0: return False

    div = 1
    while x >= 10 * div:
        div*=10

    while x >= 0:
        right = x % 10
        left = x // div

        if left != right: return False

        x = (x % div) // 10
        div = div / 100
    return True

def isPalidrome(x):
    if str(x)== str(x)[::-1]:
        return True
    else:
        return False

print(isPalidrome(121))