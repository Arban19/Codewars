# this program finds the sum of all multiples of n below m; keeping in mind n and m are natural numbers (positive integers) and m is excluded from the multiples

def sum_mul(n,m):
    if n <= 0 or m <= 0:
        return "INVALID"
    sum = 0
    for item in range(n,m):
        if item % n == 0:
            sum += item
    return sum

SumN = sum_mul(2,9)
print(SumN)

# sentence = "Duke is a good boy"
# first_word = sentence.split()[0].upper()

# # sentence.split()[0].upper() -> first_word
# print(first_word)

     
strings = "duke is a sexy boy"
def capitalize_word(word):
    return word.title()

print(capitalize_word("duke is a good boy"))


# for word in "Duke is a good boy":
#     word.split()  

def add_lists(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

total = add_lists([3,4,5])
print(total)