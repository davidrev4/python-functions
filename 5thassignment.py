# Question 1
def string(string1, string2):
    intersection = set(string1).intersection(set(string2))
    return "".join(intersection)
new_string = "the intersection is ", string(input("please put in the first word "), input("please put in the last word "))
print (new_string)

# Question 2
def number(num1, num2, num3):
    sum = 0
    for num in range(num1, num3+1):
            sum = sum + num
            global average
            average = sum / 3
    return average

print("the average is ", number(int(input("please put in the 1st number ")), int(input("please put in the 2nd number ")), int(input("please put in the last number"))))