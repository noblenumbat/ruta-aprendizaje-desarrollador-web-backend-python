# Algortihm for Palindrome
# es una palabra que se lee igual de atrás hacia adelante

str = 'racecar'

#Un algoritmo es una serie de pasos para resolver un problema
#Desglose:
#1. Comprobar si el primer indice es igua al indice en el final de la cadena
#   [0] == [6]

#2. Desglosar el problema en problemas más pequeños
#   [0] == [6]
#   [1] == [5]
#   [2] == [4]

#3. Comprobar que estas condiciones son verdaderas o falsas

# def isPalindrome(str):
#     startIndex = 0
#     endIndex = len(str)-1

#     for x in str:
#         if str[startIndex] != str[endIndex]:
#             return False
#         return True
#Nota: 💩 este algoritmo solo hace una comparación

#-----------------Versión mejorada 😎------------------------------
def isPalindrome(str):
    startIndex = 0
    endIndex = len(str)-1

    while startIndex < endIndex:
        if str[startIndex] != str[endIndex]:
            return False
        startIndex += 1
        endIndex -= 1
    return True

print(isPalindrome('racecar'))











# def isPalindrome(str):

#     es_palindrome = []

#     for x in str:
#         es_palindrome.append(x)
#     es_palindrome.reverse()
#     if ''.join(es_palindrome) == str: #se convierte la lista invertida en una cadena 
#         return 'La secuencia es palindrome'
#     else:
#         return 'La secuencia no es palindrome'

# print(isPalindrome('olo'))