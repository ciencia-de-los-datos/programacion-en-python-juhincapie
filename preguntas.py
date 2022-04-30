"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    x = [int(z[1]) for z in file_csv]
    x = sum(x)
    return x


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    from collections import Counter
    from operator import itemgetter

    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    y= [z[0] for z in file_csv]
    y=Counter(y).most_common(30)
    y.sort(key=itemgetter(0))
    return y


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    file_csv = [z[:2] for z in file_csv]
    
    result={}
    for letra,valor in file_csv:
        valor=int(valor)
        if letra in result.keys():
            result[letra].append(valor)
        else:
            result[letra]=[valor]
    result=[(key,sum(valor)) for key, valor in result.items()]
    result.sort()
    return result


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from collections import Counter
    
    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    n=[z[2].split("-") for z in file_csv]
    n=[z[1] for z in n]
    n=Counter(n).most_common(12)
    n.sort()
    return n


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    file_csv = [z[:2] for z in file_csv]
    
    result={}
    for letra,valor in file_csv:
        valor=int(valor)
        if letra in result.keys():
            result[letra].append(valor)
        else:
            result[letra]=[valor]
    result=[(key,max(valor),min(valor)) for key, valor in result.items()]
    result.sort()
    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    file_csv = [z[4] for z in file_csv]
    
    file_csv = [z.split(",") for z in file_csv ]
    file_csv = [m.split(",") for z in file_csv for m in z]
    file_csv = [m.split(":") for z in file_csv for m in z]
    
    result={}
    for letra,valor in file_csv:
        valor=int(valor)
        if letra in result.keys():
            result[letra].append(valor)
        else:
            result[letra]=[valor]
    result=[(key,min(valor),max(valor)) for key, valor in result.items()]
    result.sort()
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    file_csv = [z[:2] for z in file_csv]
    
    result={}
    for letra,valor in file_csv:
        valor=int(valor)
        if valor in result.keys():
            result[valor].append(letra)
        else:
            result[valor]=[letra]
    result=[(key,valor) for key, valor in result.items()]
    result.sort()
    return result


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    file_csv = [z[:2] for z in file_csv]
    
    result={}
    for letra,valor in file_csv:
        valor=int(valor)
        if valor in result.keys():
            result[valor].append(letra)
        else:
            result[valor]=[letra]
    result=[(key,sorted(set(valor))) for key, valor in result.items()]
    result.sort()
    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    from collections import Counter
    
    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    file_csv = [z[4] for z in file_csv]
    
    file_csv = [z.split(",") for z in file_csv ]
    file_csv = [m.split(",") for z in file_csv for m in z]
    file_csv = [m.split(":")[0] for z in file_csv for m in z]
    
    file_csv=Counter(file_csv).most_common(30)
    file_csv.sort()
    file_csv=dict(file_csv)
    return file_csv


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    file_csv = [(z[0],z[3].split(","),z[4].split(",")) for z in file_csv]
    file_csv = [(z[0],z[1].index((z[1][-1]))+1,z[2].index((z[2][-1]))+1) for z in file_csv]
    return file_csv


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    from collections import Counter
    
    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    file_csv = [(z[3].split(",")*int(z[1])) for z in file_csv]
    p=[]
    for lista in file_csv:
        p+=lista
    #result=p.copy()
    result=Counter(p).most_common(30)
    result.sort()
    result=dict(result)
    return result


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    file_csv= open("data.csv", "r").readlines()
    file_csv = [z.replace("\n", "") for z in file_csv]
    file_csv = [z.split("\t") for z in file_csv]
    file_csv = [(z[0],z[4]) for z in file_csv]
    file_csv = [(z[0],z[1].split(",")) for z in file_csv]
    file_csv = [(z ,int(m.split(":")[1])) for z,y in file_csv for m in y]

    result={}
    for letra,valor in file_csv:
        valor=int(valor)
        if letra in result.keys():
            result[letra].append(valor)
        else:
            result[letra]=[valor]
    result=[(key,sum(valor)) for key, valor in result.items()]
    result.sort()
    result=dict(result)
    return result
