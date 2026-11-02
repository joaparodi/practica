exist_path = grafo.exist_path('Puerto Madero', 'Puerto de Rodas')

if exist_path:
    paths = grafo.dijkstra('Puerto Madero')#lugar del que parto

    destination = 'Puerto de Rodas'#lugar al que quiero llegar

    peso_total = None

    camino_completo = []

    while paths.size() > 0:
        value = paths.pop()
        if value[0] == destination:#evalua hasta llegar y despues vuelve en reversapor el camino
            if peso_total is None:
                peso_total = value[1]  # Guarda el peso total acumulado
            camino_completo.append(value[0])  # Agrega el nodo al camino
            destination = value[2]  # Actualiza el destino al nodo anterior ("de dónde vino")
    camino_completo.reverse()
    print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')