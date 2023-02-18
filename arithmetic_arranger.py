def operation(up,op, lo):
    if op == '-':
        return int(up)-int(lo)
    else:
        return int(up)+int(lo)

def arithmetic_arranger(problems, calculate=False):
    upper = []
    operator = []
    lower = []
    results = []
    arranged_problems = ''
    numbers ='1,2,3,4,5,6,7,8,9,0'
    '''
    ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
       32      3801      45      123
    + 698    -    2    + 43    +  49
    -----    ------    ----    -----

    '''
    temp_list = []
    for i in problems:
        temp_list.append(i.split())
    for i in temp_list:
        upper.append(i[0])
        operator.append(i[1])
        lower.append(i[2])
    data = [upper] + [lower]
    if len(upper) > 5:
        return('Error: Too many problems')
    for i in operator:
        if str(i) != str('+') and i != str('-'):
            return('Error: Operator must be "+" or "-".')

    for i in data:
        for j in i:
            for k in list(j):
                if k not in numbers:
                    return('Error: Numbers must only contain digits.')
                elif len(list(j)) > 4:
                    return('Error: Numbers cannot be more than four digits.')
    col_widths = [max(map(len, col))+2 for col in zip(*data)]
    if calculate:
        for up, op, lo in zip(upper,operator, lower):
            results.append(str(operation(up, op, lo)))

    arranged_problems += "    ".join((val.rjust(width) for val, width in zip(data[0], col_widths)))
    arranged_problems += "\n"
    arranged_problems += "    ".join((operat.ljust(2)+value.rjust(width-2)) for operat, value, width in zip(operator, data[1], col_widths))
    arranged_problems += "\n"
    arranged_problems += "    ".join([("-"*i+"") for i in col_widths])
    if calculate:
        arranged_problems += "\n"
        arranged_problems += "    ".join((val.rjust(width) for val, width in zip(results, col_widths)))
    return arranged_problems

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True))
# python map function - map() function returns a map object(which is an iterator) of the results after applying the given
# function to each item of a given iterable (list, tuple etc.)
"""
for example:
def addition(n):
    return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(result)
>[2,4,6,8]

We can use lambda expression to achieve the same goals:
results = map(lambda x: x + x, numbers)

Python zip() method takes iterable or containers and returns a single iterator
object, having mapped values from all the containers.

"""
