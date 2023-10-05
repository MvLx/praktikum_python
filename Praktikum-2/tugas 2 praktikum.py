# print('''pilih gender anda
# 1.pria
# 2.wanita''')
# gender =input('= ')


# T = float(input('masukkan tinggi badan (cm) = '))
# B = float(input('masukkan berat badan (kg) = '))

# T = T / 100 #ini untuk mengubah cm ke m
# BMI = B/T**2

# if gender == '1' :
#     if BMI < 18 :
#         print(f"Anda tergolong Underweight dengan BMI {BMI:.2f}")
#     elif BMI >= 18 and BMI < 23.9 :
#         print(f"Anda tergolong Normal dengan BMI {BMI:.2f}")
#     elif BMI >= 24 and BMI < 26.9 :
#         print(f"Anda tergolong Overweight dengan BMI {BMI:.2f}")
#     else :
#         print(f'anda tergolong Obese dengan BMI {BMI:.2f}')        
# elif gender == '2' :
#     if BMI < 17:
#         print(f"Anda tergolong Underweight dengan BMI {BMI:.2f}")
#     elif BMI >= 17 and BMI < 23.9 :
#         print(f"Anda tergolong Normal dengan BMI {BMI:.2f}")
#     elif BMI >= 24 and BMI < 27.9 :
#         print(f"Anda tergolong Overweight dengan BMI {BMI:.2f}")
#     else :
#         print(f'anda tergolong Obese dengan BMI {BMI:.2f}')        
# else:
#     print('gender tidak ada')
# #NOMER 1



# inp1 = input('masukkan input pertama : ')
# if inp1 not in ['vertebrado', 'invertebrado'] :
#     print('input invalid')
#     exit()

# inp2 = input('masukkan input kedua : ')
# if inp2 not in ['ave','mamifero', 'inseto','anelideo'] :
#     print('input invalid')
#     exit()

# inp3 = input('masukkan input ketiga : ')

# match inp1,inp2,inp3 : 
#     case "vertebrado",'ave','carnivoro' :
#         print('aguia')
#     case "vertebrado",'ave','onivoro' :
#         print('pomba')
#     case "vertebrado",'mamifero','onivoro' :
#         print('homem')
#     case "vertebrado",'mamifero','herbivoro' :
#         print('vaca')
#     case "invertebrado",'inseto','hematofago' :
#         print('pulga')
#     case "invertebrado",'inseto','herbivoro' :
#         print('lagarta')
#     case "invertebrado",'anelideo','hematofago' :
#         print('sanguessuga')
#     case "invertebrado",'anelideo','onivoro' :
#         print('minhoca')
#     case _ :
#         print('invalid input')
# # NOMER 2


G = input('Golongan = ')
D = float(input('Daya = '))
P = float(input('Pemakaian = '))

match G :
    case "R1" :
        if D == 900 :
            T = P * 1352 
            print(f'maka jumlah tagihan anda sebesar : Rp.{T:,.01f}')
        elif D == 1300 :
            T = P * 1444.70
            print(f'maka jumlah tagihan anda sebesar : Rp.{T:,.1f}')
        elif D == 2200 :
            T = P * 1444.70
            print(f'maka tagihan anda sebesar : Rp.{T:,.1f}')
    case "R2" : 
        if D >= 3500 and D < 5500 :
            T = P * 1699.53
            print(f'maka tagihan anda sebesar : Rp.{T:,.1f}')
    case "R3" : 
        T = P * 1699.53
        if D >= 6600 :
            print(f'maka tagihan anda sebesar : Rp.{T:,.1f}')
    case "B2" : 
        T = P * 1444.70
        if D >= 6600 and D <= 200000 :
            print(f'maka tagihan anda sebesar : Rp.{T:,.1f}')
    case "B3" : 
        T = P * 1114.74
        if  D > 200000 :
            print(f'maka tagihan anda sebesar : Rp.{T:,.1f}')
        elif D < 200000 :
            print(f"data tidak valid")
    case "I3" : 
        T = P *  1314.12
        if D >= 200000 :
            print(f'maka tagihan anda sebesar : Rp.{T:,.1f}')
    case "P1" : 
        T = P * 1523.28
        if D >= 6600 and D <= 200000 :
            print(f'maka tagihan anda sebesar : Rp.{T:,.1f}')
    case _ :
        print('data tidak valid')
# # NOMER 3