# Concatenar cadenas de caracteres.

""" organizacion = "freeCodeCamp"
owner = "Jon"

print("Aprende a programar con " + organizacion)
print("Aprende a programar con {}".format(organizacion))
print("Aprende a programar con {1} {0}".format(organizacion,owner))
print(f"Aprende a programar con {organizacion}") # f-string """

# Mad Libs (Historias Locas)

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")

madlib = f"Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!" 

print(madlib)