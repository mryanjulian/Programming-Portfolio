r = 152./2**9

def bintostring(r):
    remainder = r
    result = '0.'
    count = 0
    while remainder > 0 and count < 32:
        remainder = 2*remainder
        if remainder >= 1:
            result += '1'
            remainder -= 1
        else:
            result += '0'
        count += 1
    return result

print bintostring(r)