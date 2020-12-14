import pickle

class Persona():
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        print("se ha creado una nueva persona: " , self.nombre)

    def __str__(self):
        return "{}{}{}".format(self.nombre, self.edad, self.sexo)

class listaPersonas():
    listaP = []
    # se va a hacer connstrcutor para colocar la info en el fichero
    def __init__(self):
        listaDePersonas = open("ficheroEpersonas", "ab+")
        listaDePersonas.seek(0)

        try:
            self.listaP = pickle.load(listaDePersonas)
            print("hay {} personas".format(len(self.listaP)))
        except:
            print("fichero vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)



    def agregarPersona(self, p):
        self.listaP.append(p)
        self.guardarPersonasenelFichero()

    def mostrarPersona(self):
        for p in self.listaP:
            print(p)

    def guardarPersonasenelFichero(self):
        listaDePersonas =open("ficheroEpersonas", "wb")
        pickle.dump(self.listaP, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarLaInfoDelFichero(self):
        print("la info del fichero es la siguiente: ")
        for p in self.listaP:
            print(p)

milista = listaPersonas()
persona = Persona(" mario ", " masculino ", 33)
milista.agregarPersona(persona)

milista.mostrarLaInfoDelFichero()