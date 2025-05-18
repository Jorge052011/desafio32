Peso_kg = float(input("Ingresa tu peso en kg: "))
Altura_mt =(float(input("ingresa tu altura en centimetros: ")))/100

IMC = Peso_kg / (Altura_mt * Altura_mt)

print(f"Tu índice de masa corporal (IMC) es: {IMC:.2f}")

if IMC < 18.5:
    print("La clasificación OMS es bajo de peso")
elif 18.5 <= IMC < 25:
    print("La clasificación OMS es es adecuado")
elif 25 <= IMC < 30:
    print("La clasificación OMS es sobrepeso")
elif 30 <= IMC < 35:
    print("La clasificación OMS es obesidad tipo I")
elif 35 <= IMC < 40:
    print("La clasificación OMS es obesidad tipo II")



else:
    print("La clasificación OMS es obesidad tipo III")
