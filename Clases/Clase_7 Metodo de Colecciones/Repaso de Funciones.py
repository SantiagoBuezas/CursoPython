# Problema: construir una agenda


# Idea
# Vamos a construir una agenda sobre un dict de python. Vamos a construir funciones que nos permitan,
# como usuarios realizar las siguientes operaciones:

# Consultar el email de un contacto conociendo sólo su nombre
# Agregar un contacto a la agenda
# Borrar un contacto de la agenda
# Modificar el email de un contacto en la agenda
# Modificar el nombre de un contacto en la agenda.

def consultar_el_email(un_nombre):
    print(agenda[un_nombre])

def agregar_contacto_a_agenda(un_nombre,un_email,una_agenda):
    una_agenda[un_nombre] = un_email
    print(una_agenda)
    return una_agenda
    

def borrar_cotacto_de_la_agenda(un_nombre, una_agenda):
    del una_agenda[un_nombre]
    print(una_agenda)
    return una_agenda
    

def modificar_email_de_la_agenda(un_nombre, email_nuevo, una_agenda):
    una_agenda[un_nombre] = email_nuevo
    print(una_agenda)
    return una_agenda


def modificar_nombre_de_la_agenda(nombre_a_cambiar, nombre_nuevo, una_agenda):
    una_agenda[nombre_nuevo] = una_agenda.pop(nombre_a_cambiar)
    print(una_agenda)
    return una_agenda

agenda = dict()
print(agenda)

agregar_contacto_a_agenda("Mariano","Mariano@coder.com", agenda)
agregar_contacto_a_agenda("Juan","Juan@coder.com", agenda)
agregar_contacto_a_agenda("Santiago","sbues2@gmail.com", agenda)
agregar_contacto_a_agenda("Sabrina","sdibernardo@hotmail.com", agenda)
consultar_el_email("Mariano")
borrar_cotacto_de_la_agenda("Juan", agenda)
modificar_email_de_la_agenda("Sabrina","SabrinaDiBernardo@gmail.com",agenda)
modificar_nombre_de_la_agenda("Mariano","Matias",agenda)
print("*" * 100)

print(agenda)