#ZhanaiymDauken 
#Laba1 zhane 2
#Натурал санды енгіземіз.  Осы санды құрайтын цифрлардың қосындысы мен көбейтіндісін табу.   егер санда 0 саны кездессе, онда мәнді табу кезінде оны есепке алмау керек

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
