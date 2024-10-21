from collections import namedtuple
import csv

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero: str) -> list:
    """lee el fichero de entrada y devuelve una lista de tuplas de tipo RegistroPoblacion.

    :param ruta_fichero: ruta de un fichero csv
    :type ruta_fichero: str
    :return: lista de tuplas de tipo RegistroPoblacion
    :rtype: list
    """    
    registros = []
    with open(ruta_fichero, encoding='utf-8') as f:
        lector_csv = csv.reader(f)

        #Itera sobre las filas y crea tuplas:
        for fila in lector_csv:
            pais, codigo, año, censo = fila
            registros.append(RegistroPoblacion(pais, codigo, int(año), int(censo)))
    
    return registros 


def calcula_paises(poblaciones: list) -> list:
    """toma una lista de tuplas de tipo RegistroPoblacion y devuelve una lista ordenada alfabéticamente con los nombres de los países para los que hay datos.

    :param poblaciones: lista de tuplas de tipo RegistroPoblacion
    :type poblaciones: list
    :return: lista ordenada alfabéticamente con los nombres de los países para los que hay datos
    :rtype: list
    """    

    conj_nombres_paises = set()

    for e in poblaciones:
        conj_nombres_paises.add(e.pais)     #vamos añadiendo los paises al conjunto
    
    list_nombres_paises = list(conj_nombres_paises)           #convertimos el conjunto en una lista 
    
    list_nombres_paises.sort()
    return list_nombres_paises


def filtra_por_pais(lista: list, nombre_o_codigo: str) -> list:
    """toma una lista de tuplas de tipo RegistroPoblacion, y el nombre o código de un país, y devuelve una lista de tuplas con los datos del país que se pasa como parámetro (año y censo)

    :param lista: lista de tuplas de tipo RegistroPoblacion
    :type lista: list
    :param nombre_o_codigo: el nombre o código de un país
    :type nombre_o_codigo: str
    :return: lista de tuplas con los datos del país que se pasa como parámetro
    :rtype: list
    """    
    lista_pais_unico = []
    for e in lista:
        if nombre_o_codigo in (e.pais, e.codigo):
            lista_pais_unico.append((e.año, e.censo))

    return lista_pais_unico

def filtra_por_paises_y_año(poblaciones: list, año: int, paises: set) -> list:  
    """toma una lista de tuplas de tipo RegistroPoblacion, un año y un conjunto de nombres de países, y devuelve una lista de tuplas (nombre_pais, num_habitantes) con los datos del año pasado como parámetro para los países incluidos en el parámetro paises.

    :param poblaciones: lista de tuplas de tipo RegistroPoblacion
    :type poblaciones: list
    :param año: un año
    :type año: int 
    :param paises: conjunto de nombres de paises 
    :type paises: set 
    :return: lista de tuplas (nombre_pais, num_habitantes) con los datos del año pasado como parámetro para los países incluidos en el parámetro paises
    :rtype: list
    """    

    lista_pais_numHab = []
    for e in poblaciones:
        if (e.pais in paises) and (e.año == año):
            lista_pais_numHab.append((e.pais, e.censo))
    
    return lista_pais_numHab