Pokémon = {}

def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, animal, digite um número válido")
def cadastrar(alunos): 
    nome = input("Nome: ").strip().title()
    nota = ler_float("Nota: ")
    alunos[nome] = {"notas": nota}


cadastrar(Pokémon)
print(Pokémon)