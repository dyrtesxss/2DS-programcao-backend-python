aluno = {"nome": "Ana", "nota": 9.0}

if "nota" in aluno:
    print("Nota cadastrada")

for chave, valor in aluno.items():
    print(chave, "-->", valor)