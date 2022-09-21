n = int(input("Введите число:"))
suma=0
mult = 1
while(n > 0):
    dig = n % 10
    if dig !=0:
        suma+=dig
        mult*=dig
    n = n//10
print("Сумма цифр равна:", suma)
print("произведение:",mult)
