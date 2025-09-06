# Herança, exemplo para entendimento: Criação da Classe Família em Python 

Este projeto, desenvolvido por mim, **Michele**, demonstra o uso de **Programação Orientada a Objetos (POO)** em Python, utilizando o conceito de **herança de classes** para representar uma família.

## Estrutura

- **Classe base:** `Familia`
  - Atributos: `sobrenome`, `comida_preferida`, `origem`
  - Métodos: `comer_receita()`, `contar_historia()`

- **Classes derivadas:**
  - `Pai` → adiciona o atributo `profissao` e o método `trabalhar()`.
  - `Mae` → adiciona o atributo `curso` e o método `estudar()`.
  - `Filho` → adiciona o atributo `brinquedo_favorito` e o método `brincar()`.

## Exemplo de uso

```python
pai = Pai("Silva", "Moqueca de peixe", "Bahia", profissao="Administrador")
mae = Mae("Silva", "Moqueca de peixe", "Bahia", curso="História da Arte")
filho = Filho("Silva", "Moqueca de peixe", "Bahia", brinquedo_favorito="Lego")

pai.contar_historia()
pai.comer_receita()
pai.trabalhar()

mae.estudar()
filho.brincar()
