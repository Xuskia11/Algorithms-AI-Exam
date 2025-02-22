def conv_num(num, type):
    if type == "decimal_to_binary":
        binary = ""
        while num > 0:
            binary = str(num % 2) + binary
            num = num // 2
        if binary:
            return binary
        else:
            return "0"
    elif type == "binary_to_decimal":
        number = 0
        pow = 0
        for i in reversed(num):
            if i == "1":
                number += 2 ** pow
            pow += 1
        return number
    else:
        return "Invalid type"
        

print(conv_num("111000","binary_to_decimal"))
print(conv_num(56,"decimal_to_binary"))