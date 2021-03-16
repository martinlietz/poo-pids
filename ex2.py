class Jogador:
  # o método __init__ é obrigatório e é executado ao fazer Jogador()
  def __init__(self, id, nome, idade, points = 0):
    self.id = id
    self.nome = nome
    self.idade = idade
    self.pontuacao = points

  def alteraNome(self, novoNome):
    self.nome = novoNome

class Animal:
  def __init__(self, species, region, population):
    self.especie = species
    self.regiao = region
    self.populacao = population

  def reproduzir(self, quantidade):
    # Animal.reproduzir(self, 100)
    self.populacao = self.populacao + quantidade

  def alimentar(self):
    self.reproduzir(100)

player1 = Jogador('Ana', 20, 90)
player2 = Jogador('Felipe', 29, 80)

player1.alteraNome("Marcela")
print(player1.nome)

caes = Animal('canis lupus', 'indeterminado', 100e7)
caes.reproduzir(2)
caes.reproduzir(10)
caes.alimentar()

print(caes.populacao)


