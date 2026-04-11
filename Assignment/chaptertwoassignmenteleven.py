userinput = input("Enter a five digit integer: ")

firstdigit = int(userinput)//10
firstdigitrem = int(userinput) % 10

seconddigit = firstdigit//10
seconddigitrem = firstdigit % 10

thirddigit = seconddigit//10
thirddigitrem = seconddigit % 10

fourthdigit = thirddigit//10
fourthdigitrem = thirddigit % 10

fifthdigit = fourthdigit//10
fifthdigitrem = fourthdigit % 10

print(firstdigitrem, "   ", seconddigitrem, "    ", thirddigitrem, "     ", fourthdigitrem, "    ",fifthdigitrem)
