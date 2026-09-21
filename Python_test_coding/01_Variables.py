# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print

print(my_string_variable, str(my_int_variable), my_bool_variable)
print("Hier ist bool e int:", my_bool_variable, my_int_variable)
      
# Algunas funciones del sistema

print(len(my_string_variable))

# Variables en una sola línea

name, surname, alias, age = "Cristobal", "Sanchez", "Cris", 19
print("Ich heisse:", name, surname,", Mein alias ist:", alias,
      ", und ich bin:", age,"jahre alt")

# Inputs

"""
name = input("Wie heisst du?: ")
age = input("Wie alt bist du?: ")

print(name)
print(age)
"""

# Cambiar su tipo

name = 35
age = "Cris"
print(name)
print(age)

# Forzando el tipo

address: str = "Mein adresse"
address = 32
print(type(address))

# Test

first_name = "Cristobal Ignacio"
last_name = "Sanchez Mardones"
age = 19
tag, monat, jahr = "27", "Jan", "2007"
country = "Chile"
city = "Santiago"
is_single = False
Skills = ["VideoSpiele","Deutsch","English","Spanisch."]
person_info = {
    "firstname" : "Cristobal Ignacio",
    "lastname" : "Sanchez Mardones",
    "age" : 19,
    "country" : "Chile",
    "city" : "Santiago",
}

print("Vorname:", first_name)
print("Nachname:", last_name)
print("Land:", country)
print("Statdt:", city)
print("Alter:", age,"Jahre alt")
print("Geboren am:", tag, monat, jahr)
print("Verheirated:", is_single)
print("Fähigketiten:", Skills)
print("Persönliche Angaben:", person_info)
