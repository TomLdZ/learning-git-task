shopping_dict = {"piekarnia":["chleb", "pączek", "bułki"], "warzywniak":["marchew", "seler", "rukola"]}

prod_quantity = 0

raport_parts = []

raport_parts.append("Lista zakupów:")

for shop in shopping_dict:
    list_capitalized = list(item.capitalize() for item in shopping_dict[shop])
    raport_parts.append(f"Idę do {shop.capitalize()}, kupuję tu następujące rzeczy: {list_capitalized}")
    prod_quantity += len(list_capitalized)

raport_parts.append(f"W sumie kupuję {prod_quantity} produktów")

raport = "\n".join(raport_parts)

print(raport)