"""
26. Pedir una nota entera de 0 a 10 y mostrarla de la siguiente forma:
• Insuficiente (de 0 a 4).
• Suficiente (5).
• Bien (6).
• Notable (7 y 8).
• Sobresaliente (9).
• Matrícula de honor (10).

"""
nota = int(input("Introduce nota: \n"))
notas = {5: "Suficiente", 6: "Bien", 7: "Notable", 8: "Notable", 9: "Sobresaliente", 10: "Matricula de honor"}

if nota <= 4:
    print("Suspenso")
else:
    print(f"{notas[nota]} ({nota}).")