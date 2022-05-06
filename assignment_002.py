#Q1.........................................................................
input_str = "Python is a case sensitive language"
print(input_str)


#PART a
#len() function is used to find length of string
string_length = len(input_str)
print("Length of the string is:", string_length)


#PART b
string_reverse = input_str[::-1]
print("The reversed string is:",string_reverse)


#PART c
#Using slice to store a part of string in a variable
string_slice = input_str[10:26]


#PART d
#repalcing the stored sliced string 
replaced_string = input_str.replace(string_slice, "object oriented")
print(replaced_string)


#PART e (Index of "a")
index_a = input_str.find("a")
print('''Index of "a" in input string is:''',index_a)


#PART f
#replacing spaces with empty quotes to remove white spaces
m = input_str.replace(" ", "")

print(m)


#Q2..............................................................................


name = "NAVYA"
SID = "21107088"
CGPA = "7.9"
department_name = "MECHANICAL"


print("Hey,",name, "Here!\nMy SID is", SID,"\nI am from", department_name, "department and my CGPA is", CGPA )


#Q3.....................................................................................


a = 56
b = 10
print("a =",a, "b =", b)

#PART a
and_function = a&b
print("Value of a&b:", and_function)


#PART b
or_function = a|b
print("Value of a|b:",or_function)


#PART c
xor_function = a^b
print("Value of a^b:",xor_function)


#PART d
left_shift = a<<2, b<<2
print("Value after left shifting both a and b by 2 bits.:",left_shift)


#PART e
right_shift = a>>2, b>>4
print("Value after right shifting both a by 2 bits and b by 4 bits.:",right_shift)


#Q4....................................................................................


print('''This code checks if input by user has the word "name" in it.''')
print('''You get "Yes" and "No" accordingly.''')


input_user = input("enter the input string: ")


#Using 'in' operator to find "name" in input string
true_or_false = "name" in input_user


#Using 'if else' to produce "Yes" and "No"
if true_or_false == True:
    print("Yes")

else:
    print("No")


#Q5..............................................................................


side_1 = float(input("Enter length 1:"))
side_2 = float(input("Enter length 2:"))
side_3 = float(input("Enter length 3:"))


#converting into integers, use 'round' function
side_1 = int(round(side_1))
side_2 = int(round(side_2))
side_3 = int(round(side_3))


x = side_1 + side_2
y = side_2 + side_3
z = side_1 + side_3


#If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle.
check_1 = x > side_3
check_2 = y > side_1
check_3 = z > side_2


#Checking if the three conditions are true or false
#Using 'and' function on all three because all need to be true for a triangle to be formed

ans = str(check_1 & check_2 & check_3)
ans = ans.replace("True", "Yes")
ans = ans.replace("False", "No")

print("Can a triangle be formed?"  , ans)


#Q6...............................................................................


number_1 = int(input("Enter 1st number (a): "))
number_2 = int(input("Enter 2nd number (b): "))


'''Using 'exor' function as it gives output "0" for input values (0,0 and 1,1) and output "1" for input values (0,1 and 1,0)
Therefore, when we will have different values, we will get "1"and we will need to replace that bit to make the numbers same.
We will count the number of 1s that come in binary after 'exor' operation to check how many bits we need to flip to convert 
'a' to 'b' as asked in question'''

exor_function = number_1 ^ number_2


bin_exor = bin(exor_function)
check_string = str(bin_exor)


bits_flip = check_string.count("1")

print('''Number of bits needed to be flipped to convert "a" to "b" are: ''', bits_flip)