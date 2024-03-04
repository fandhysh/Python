tahun = 1990

def pengulangan(tahun):
    if tahun / 4 == 0 :
      leap = True
    elif tahun / 100 == 0 :
       leap = False
    elif tahun / 400 == 0 :
        leap = True
    return leap

print(pengulangan(tahun))

#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.