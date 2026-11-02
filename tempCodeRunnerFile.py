grafo = Graph(is_dir=False)# H


# vertices = {
#     # Routers
#     "Router 1": "router",
#     "Router 2": "router",
#     "Router 3": "router",
    
#     # Switches
#     "Switch 1": "switch",
#     "Switch 2": "switch",
    
#     # Servidores
#     "Guarani": "servidor",
#     "MongoDB": "servidor",
    
#     # Impresora
#     "Impresora": "impresora",
    
#     # Notebooks (triángulos azules)
#     "Red Hat": "notebook",
#     "Debian": "notebook",
#     "Arch": "notebook",
    
#     # PCs (cuadrados amarillos)
#     "Ubuntu": "pc",
#     "Mint": "pc",
#     "Manjaro": "pc",
#     "Fedora": "pc",
#     "Parrot": "pc"
# }

# aristas_completo = [
#     # Router 2
#     ("Router 2", "Red Hat", 25),
#     ("Router 2", "Guarani", 9),
#     ("Router 2", "Router 3", 50),
#     ("Router 2", "Router 1", 37),
    
#     # Router 1
#     ("Router 1", "Router 3", 43),
#     ("Router 1", "Switch 1", 29),
    
#     # Switch 1 y sus dispositivos
#     ("Switch 1", "Debian", 17),
#     ("Switch 1", "Ubuntu", 18),
#     ("Switch 1", "Impresora", 22),
#     ("Switch 1", "Mint", 80),
    
#     # Router 3 hacia Switch 2
#     ("Router 3", "Switch 2", 61),
    
#     # Switch 2 y sus dispositivos / conexiones
#     ("Switch 2", "Manjaro", 40),
#     ("Switch 2", "Fedora", 3),
#     ("Switch 2", "Parrot", 12),
#     ("Switch 2", "MongoDB", 5),
   
#     ("Switch 2", "Arch", 56)
# ]

# # A
# def cargar_grafo(grafo: Graph, vertices):
#     for nombre, tipo in vertices.items():
#         grafo.add_vertex(nombre , tipo)


# cargar_grafo(grafo, vertices)

# def cargar_aristas(grafo: Graph, aristas_completo):
#     for origen, destino, peso in aristas_completo:
#         grafo.add_edge(peso, origen, destino)

# cargar_aristas(grafo, aristas_completo)
