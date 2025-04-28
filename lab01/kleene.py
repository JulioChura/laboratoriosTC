def clausula_kleene(lenguaje, maxNumCaracteres):

    kleene_list = [""]  # incluir la cadena vacía

    while True:
        nuevas_cadenas = []
        for cadena_existente in kleene_list:
            for palabra in lenguaje:

                if cadena_existente == "":
                    nueva = palabra
                else:
                    nueva = cadena_existente + palabra
                    
                if len(nueva) > maxNumCaracteres:
                    kleene_list.extend(nuevas_cadenas)
                    return kleene_list
                if nueva not in kleene_list:
                    nuevas_cadenas.append(nueva)
        
        kleene_list.extend(nuevas_cadenas)

    