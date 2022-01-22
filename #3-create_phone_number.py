# problem link : https://www.codewars.com/kata/525f50e3b73515a6db000b83
def create_phone_number(n):
    # my solution
    return "({0}) {1}-{2}".format(''.join(map(str, n[:3])),''.join(map(str, n[3:6])),''.join(map(str,n[6:])))
    # the best solution
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)