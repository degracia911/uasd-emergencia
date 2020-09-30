def e2():
    contactos = []
    class clsContacto () :
        nombre = ""
        apellido= ""
        telefono = ""
    while True:
        print("Bienvenido a la AGENDA");
        print("1 si desea agregar un contacto")
        print("2 si desea ver un contacto");
        print("3 si desea eliminar un contacto");
        opcion = input("Escriba una opcion :  ");
        if opcion == "1" :
            print("Agregar Contacto");
            contacto =  clsContacto ()
            contacto.nombre = input("Escriba un nombre");
            contacto.apellido = input("Escriba un apellido");
            contacto.telefono = input("Escriba un telefono");
            contactos.append (contacto)
        elif opcion == "2" :
            print("Contactos agregados");
            for contacto in contactos :
                print("nombre \t apellido  \t telefono");
                print(contacto.nombre + "\t" +contacto.apellido + "\t" +contacto.telefono);
                input()
                e2();

e2() 





