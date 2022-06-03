class Lluvia:
    def __init__(self,mm):
        self.cantidad = mm


    def reportaje(self,reportaje):
        print (reportaje)

Mayo = Lluvia(3020.25)
Abril = Lluvia(991.2)


print ("Cantidad de lluvia (mm) en Mayo: ", Mayo.cantidad)
print ("Cantidad de lluvia (mm) en Abril: ", Abril.cantidad)

Mayo.reportaje("En Mayo hubo precipitación alta")
Abril.reportaje("En Abril hubo precipitación baja")
