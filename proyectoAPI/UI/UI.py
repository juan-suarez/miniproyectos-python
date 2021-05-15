import sys 
sys.path.append("..")
from API import Api
from tabulate import tabulate
all_deparments = ['AMAZONAS','ANTIOQUIA','ARAUCA','ATLANTICO','BOLIVAR','BOYACA','CALDAS','CAQUETA','CASANARE','CAUCA','CESAR','CHOCO',
'CORDOBA','CUNDINAMARCA','GUAINIA','GUAVIARE','HUILA','GUAJIRA','MAGDALENA','META','NARIÑO','NORTE DE SANTANDER','PUTUMAYO','QUINDÍO',
'RISARALDA','SAN ANDRES Y PROVIDENCIA','SANTANDER','SUCRE','TOLIMA','VALLE','VAUPES','VICHADA']
def menu ():
    print("BIENVENIDO")
    while True:
        TrueDeparment = True
        limit= int (input ("Ingrese el numero maximo de datos a buscar: "))
        while TrueDeparment:
            deparment =input("Ingrese el departamento(sin tilde): ")
            deparment = deparment.upper()
            if deparment not in all_deparments:
                print("Departamento no encontrado.")
                continue
            TrueDeparment = False
        result =Api.consult(limit,deparment)
        print(tabulate(result, 
                headers=['Ciudad', 'Departamento', 'Edad', 'Tipo', 'Estado', 'Procendencia'], 
                tablefmt='fancy_grid',
                stralign='center'))
        next = input("Desea buscar mas datos?[Y/N]: ")
        if next == "N" or next == "n":
            break