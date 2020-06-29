number = int(input())
word_ = str(input())

# write a condition for plurals
if number == 0 or number > 1:
    word_ = (word_ + 's')

print(number, word_)