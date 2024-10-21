from poblacion import *

def lee_poblaciones_test(ruta):
    print('====Testeando función lee_poblaciones====')
    res = lee_poblaciones(ruta)
    print(res)

def calcula_paises_test(lista):
    print('====Testeando función calcula_paises====')
    print(calcula_paises(lista))

def filtra_por_pais_test(lista, nombre_o_codigo):
    print('====Testeando función filtra_por_pais====')
    print(filtra_por_pais(lista, nombre_o_codigo))

def filtra_por_paises_y_año_test(poblaciones, año, paises):
    print('====Testeando función filtra_por_paises_y_año====')
    print(filtra_por_paises_y_año(poblaciones, año, paises))


if __name__ == '__main__':

    #lee_poblaciones_test('data/population.csv')

    #calcula_paises_test(lee_poblaciones('data/population.csv'))

    #filtra_por_pais_test(lee_poblaciones('data/population.csv'), 'Australia')

    filtra_por_paises_y_año_test(lee_poblaciones('data/population.csv'), 1979, ('France', 'Austria', 'Australia', 'Japan'))