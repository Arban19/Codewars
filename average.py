
def find_average(numbers):
    """ This program provides the average of the input; for an empty list it will return 0 """
    if not numbers:
        return 0
    average = sum(numbers)/len(numbers)
    return average

def find_average(numbers):
    """ This program provides the average of the input; for an empty list it will return 0 """
    if len(numbers) <= 0:
        return 0
    total = 0
    for number in numbers:
        total += number
        average = total/len(numbers)
    return average
