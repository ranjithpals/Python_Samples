class India:

    # Class Public property
    capital = "New Delhi"

    def __init__(self, population, no_states=28, no_u_territories=8):
        self._population = population
        self._no_states = no_states
        self._no_u_territories = no_u_territories

    def total_provinces(self):
        return self._no_states + self._no_u_territories

    def total_population(self):
        return self._population


if __name__ == '__main__':

    # Initialize class with passing only one parameter, others assigned the default values
    i1 = India(400000)
    print(i1.total_provinces())
    print(i1.total_population())

    # Initialize class with passing two parameters, second parameter initializes first default parameter 'no_states'
    i2 = India(35500000, 30)
    print(i2.total_provinces())
    print(i2.total_population())

    print(India.capital)
    India._capital = "NCR Area"
    print("India's New Capital: {}".format(India.capital))