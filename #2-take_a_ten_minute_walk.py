# problem link : https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk):
    if len(walk) != 10 : return False
    return walk.count("s") == walk.count("n") and walk.count("e") == walk.count("w")