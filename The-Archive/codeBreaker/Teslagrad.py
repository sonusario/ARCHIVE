import numpy as np

def stepSplit(arr, arrLen, sDist):
    newArr = []
    step = int(arrLen/sDist)
    prv = 0
    nxt = step
    while nxt <= arrLen:
        newArr.append(arr[prv:nxt])
        prv = nxt
        nxt += step
    return newArr

'''
A
'''

b64 = 'f6PNUlnL5NYw3fk4DBEfRz1tey9wNRdlgfYLIbtrExEqwYfN2QyZh+WQsiuFu1sSI0pEj/ZriskbjP27i9l5u/XF3CM+yrkyzxmHHBJFmg1s4iH/dXjxBWu07cBWnVkMmdES1MvbJrQI7Uka22iHgbtrQ+tvdaNK/eBS68u++Yy5ByDwHBnKObpIO8AiJwMT9e243doRm965rxQlBSED5win2gVzrMJ9gDugNtvXb2v3XDRBhdH9OBIdIylbxwRuHEf7PEOE/Hb7Zh6VU8WKqONHSYic571a2gVu5X6V+61JTTR1EGRJ45EzU0EzXmrnDtdhi+5wBgKYWWA8g1/kWJfl387973nmPnRC02E4t4ORpUKF9K8L4SaoTG2Uhum4vOrep+o4urfDd+9LUTdzDtQGX0xjhWFmfUvh3tdDCbbQTbY0Weo8AGg8za4Gmn81cpJfRhQFyrzSDpLG0KHjRgyR9DUga3Th28NA57nNFeIM8j3AaAKKkkcR/7mWAl3Mpfb4vOcAH0iV1PEe'
c64 = 'f6PNUlnL5NYw3fk4DBEfRz1tey9wNRdlgfYLIbtrExEqwYfN2QyZh+WQsiuFu1sSI0pEj/ZriskbjP27i9l5u/XF3CM+yrkyzxmHHBJFmZqrGUljdtscrwfk4BF0OAix6bSdhM0V3wPFDI6AmHREqkoHF0gzc3qyltCDQuBMDJQVXm+YikMtH3ty40tR4uaaS0z9qhLEvmQjPEA8JhUkp82SofmL4Emux69ga0UEazJQT3MrXcrQEo0sAlXvIge90Q/hzPKRA8bBF8tO++Yy9U3DoGwnUcfsBNM12ZAAYu/ClmsAQ296ZoRV9BSUL/BiykkRrr84+iSC0fp/KLn7wFStcxIaEKQ5cP2wP2RhuEUbteBec9Xb3axnQB8uA/fAWAKqPq7ocmzkrsWWVr7gGSz91XStbrNY2XUUxBjOvHJh0iesqVW2IGHc/wl+rDIvomtO86GWjd2UD1Gp7souRq0qR++MatmeVCjqfhfHw7OzTtK8mr+TDP+tIFXF1CdwGSUB2kmVhckDtidlfAfKEQKt9WPtvGyY40a4EkToxadcZRA9LxvmfHJnOlualS1W+9Ho/ZX+ltNhD8bDNSOIs1UWaRFfeqVsTtKzUB0zM7rf8t+8aXkiU3/ge'
b64g105 = []

b64len = len(b64)
c64len = len(c64)
step = int(b64len/5)

print('b64 length:', b64len)
print('b64b length:', c64len)
print('step: ', step)

b64g105 = stepSplit(b64, b64len, 5)

'''
B
'''

h = '0101110011010111001010110110010100010001100100101001001101001010110110'
hLen = len(h)
print(len(h))

arr = stepSplit(h, hLen, 10)
rc = []
for hc in arr:
    rc.append(np.fromstring(hc, 'u1') - ord('0'))
rc = np.array(rc, dtype=int)

R = np.array([[0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 1]])

for hc in rc:
    print(np.matmul(R,hc))

