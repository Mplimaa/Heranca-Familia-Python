class Familia:
    def __init__(self, sobrenome, comida_preferida, origem):
        self.sobrenome = sobrenome
        self.comida_preferida = comida_preferida
        self.origem = origem

    def comer_receita(self):
        print(f"A comida preferida da família {self.sobrenome} é {self.comida_preferida}.")

    def contar_historia(self):
        print(f"A família {self.sobrenome} veio originalmente de {self.origem}.")


class Pai(Familia):
    def __init__(self, sobrenome, receita_de_familia, origem, profissao):
        super().__init__(sobrenome, receita_de_familia, origem)
        self.profissao = profissao

    def trabalhar(self):
        print(f"O pai da família {self.sobrenome} está trabalhando como {self.profissao}.")


class Mae(Familia):
    def __init__(self, sobrenome, receita_de_familia, origem, curso):
        super().__init__(sobrenome, receita_de_familia, origem)
        self.curso = curso

    def estudar(self):
        print(f"O mae da família {self.sobrenome} está estudando {self.curso}.")


class Filho(Familia):
    def __init__(self, sobrenome, receita_de_familia, origem, brinquedo_favorito):
        super().__init__(sobrenome, receita_de_familia, origem)
        self.brinquedo_favorito = brinquedo_favorito

    def brincar(self):
        print(f"O filho da família {self.sobrenome} está brincando com {self.brinquedo_favorito}.")


Pai = Pai("Silva", "Moqueca de peixe", "Bahia", profissao="Administrador")
Mae = Mae("Silva", "Moqueca  de peixe", "Bahia", curso="Historia da arte")
Filho = Filho("Silva", "Moqueca  de peixe", "Bahia", brinquedo_favorito="Lego")

# Pai
Pai.contar_historia()
Pai.comer_receita()
Pai.trabalhar()

print("---")

# Mae
Mae.contar_historia()
Mae.comer_receita()
Mae.estudar()

# Filho
print("---")
Filho.contar_historia()
Filho.comer_receita()
Filho.brincar()


