#Zadanie: palindromy

#Twoim zadaniem będzie napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem. Palindrom to słowo, które czytane od lewej do prawej i od prawej do lewej brzmi tak samo. Przykłady to “kajak” i “potop”.

#Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.

#for letter in "kodilla":
#    print(letter)

def palindromy (word):
    """
        Returns True or False, based on string argument passed.
        When word is a palindrome the function will return True,
        otherwise False
        Argument: word
    """
    my_bolean = True
    for i in range(len(word)):
        if word[i] != word[len(word)-i-1]:
            my_bolean = False
            return my_bolean
    return my_bolean
        

if palindromy("kajak"):
    print("To jest palindrom")       
else:
    print("To nie jest palindrom")    

