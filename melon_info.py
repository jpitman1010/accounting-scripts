"""Print out all the melons in our inventory."""


from melons import melons


def print_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon_names, attributes in melons.items():
        print(melon_names.upper())

        for attribute, descriptions in attributes.items():
            print(f"{attribute}: {descriptions}")

        print("-----------------------------------------")

print_melons(melons)


    #     have_or_have_not = 'have'
    #     if seedless:
    #         have_or_have_not = 'do not have'

    #     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


    # for i in melon_names:
    #     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])

      
