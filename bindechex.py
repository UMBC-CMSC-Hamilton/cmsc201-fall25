"""
How do we convert from decimal into hex?

Hex into Decimal?   That's what we're doing

Ex:
4       a       c
16^2    16      1
256
4 * 256 + 10 * 16 + 12 * 1 = 1024 + 160 + 12 = 1184 + 12 = 1196

In order to signal that you're using hex to python, or C++ or Java or whatever

    0x[Your hex number]

f3 into decimal [exam type question]
15 * 15 + 15 = 225 + 15 = 240 + 3 = 243 good.

b3c5 into decimal
b       3       c       5
4096    256     16      1

11 * 4096 + 3 * 256 + 12 * 16 + 5
"""
print(0x4ac)
print(0xf3)

"""
How do we convert from decimal into hex?
"""

print(hex(12345), bin(14))
print(type(hex(16)))


def decimal_to_hex_dict(num):
    hex_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

    if num == 0:
        return '0x0'
    result = ''
    while num > 0:
        result = hex_map[num % 16] + result
        num //= 16

    return '0x' + result


def decimal_to_hex(num):
    if num == 0:
        return '0x0'
    result = ''
    while num > 0:
        if 0 <= num % 16 <= 9:
            result = str(num % 16) + result
        else:
            result = chr(ord('a') + num % 16 - 10) + result
        num //= 16

    return '0x' + result


n = int(input('>> '))
while n >= 0:
    print(n, decimal_to_hex(n), hex(n), decimal_to_hex_dict(n))
    n = int(input('>> '))
