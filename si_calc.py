import math

def SI(P,T,R):
    SI = (P * T * R) // 100
    return SI

def rate(I,P,T):
    rate = I / (P * T)
    return rate

def principal(I,R,T):
    principal = I / (R * T)
    return principal

def time(I,P,R):
    time = I // math.floor(P * R)
    return time