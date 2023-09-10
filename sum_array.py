def sum_array(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

def sum_array(a):
  return sum(a)

def sum_array(a):
    new_num = 0
    for i in a:
        if str(i) in "qwertyuiopasdfghjklzxcvbnm":
            return 0
        new_num += i
    return new_num
