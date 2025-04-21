

def clausula_kleene(lenguaje, pasadas):
    kleene_list = [""]  # incluir la cadena vacía

    for i in range( pasadas ):
        nuevas_cadenas = []
        for cadena_existente in kleene_list:
            for palabra in lenguaje:
                if cadena_existente == "":
                    nueva = palabra
                else:
                    nueva = cadena_existente + palabra
                nuevas_cadenas.append(nueva)
        
        kleene_list.extend(nuevas_cadenas)

    kleene_sin_repetidos = []
    for c in kleene_list:
        if c not in kleene_sin_repetidos:
            kleene_sin_repetidos.append(c)

    return kleene_sin_repetidos
