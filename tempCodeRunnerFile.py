def by_name(item):
    return item.name

def by_species(item):
    return item.species

lista_p.add_criterion("name",by_name)
lista_p.add_criterion("species",by_species)
lista_p.sort_by_criterion("species")
lista_p.sort_by_criterion("name")


lista_p.show()