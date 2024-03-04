import re

txt = input('Masukan Password : ')

while True :
  if (len(txt)<=8):
    flag = -1
    print ('Minimum 8')
    break
  elif (len(txt)>=16):
    flag = -1
    print ('Maksimum 16')
    break
  elif not re.search("[A-Z]", txt):
    flag = -1
    print ('Minimal 1 Huruf Besar') 
    break
  elif not re.search("[a-z]", txt):
    flag = -1
    print ('Minimal 1 Huruf Kecil')
    break
  else :
    flag = 0 
    print ('password valid')

if flag == -1 :
  print ('Password tidak Valid')
 


  


#Panjang password harus antara 8 hingga 16 karakter.
#Password harus mengandung setidaknya satu huruf besar (uppercase), satu huruf kecil (lowercase), satu angka (digit), dan satu karakter khusus (special character) dari: !@#$%^&*()-_+=.
#Password tidak boleh mengandung spasi atau karakter non-ASCII.