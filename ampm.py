__author__ = 'rfischer'

T = raw_input()

n = int(T[:2])
if n == 12:
    n = 0

if T[-2:] == "PM":
    n += 12

print str(n).zfill(2) + T[2:8]

