"""
number = input('give me number')
high_score = 0
def hc_fun():
    global high_score
    if int(number) > high_score:
        high_score = number
    return high_score
hc_fun()
print(high_score)
"""
file = open('high_score')
file.write('hello')
file.close()
