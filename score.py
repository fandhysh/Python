x = int(input("Masukan Angka : "))

if x > 90:
    print("You Got A")
elif 80 <= x <= 89:
    print("You Got B")
elif 70 <= x <= 79:
    print("You Got C")
elif 60 <= x <= 69:
    print("You Got D")
elif 0 <= x <= 59:
    print("You Got E")
else:
    print("GOBLOK")


# If the score is 90 or above, the grade assigned is "A".
# If the score is between 80 and 89, the grade assigned is "B".
# If the score is between 70 and 79, the grade awarded is "C".
# If the score is between 60 and 69, the grade awarded is "D".
# If the score is between 0 and 59, the grade awarded is "E".
