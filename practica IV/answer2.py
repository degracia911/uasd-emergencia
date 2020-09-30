class Estudiantes:
    def __init__(self, promedio):
        self.promedio = promedio
        if promedio > 100:
            print("promedio maximo")
        else:
            print("promedio minimo")

Estudiante = Estudiantes(100)

