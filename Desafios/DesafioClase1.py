nombre = str(input("ingrese nombre:"));
nota_1 = float(input(f"ingrese nota 1 de {nombre}:"));
nota_2 = float(input(f"ingrese nota 2 de {nombre}:"));

nota_promedio = float((nota_1 + nota_2) / 2);
nota_ponderada_1 = float(nota_promedio * 0.4);
nota_ponderada_2 = float(nota_promedio * 0.6);

texto_promedio = f"El promedio de {nombre} es {nota_promedio}";
texto_nota_ponderada_1 = f"La nota ponderada del primer examen es {nota_ponderada_1}";
texto_nota_ponderada_2 = f"La nota ponderada del segundo examen es {nota_ponderada_2}";

print(texto_promedio);
print(texto_nota_ponderada_1);
print(texto_nota_ponderada_2);
