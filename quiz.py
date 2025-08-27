print("=== Bem-vindo ao Quiz do Aluno Patrick! ===\n")
nome = input("Qual é o seu nome? ")
print(f"\nOlá, {nome}! Vamos começar o quiz educacional 🎓\n")

pontos = 0

# Pergunta 1
print("1) Qual é a capital do Brasil?")
print("a) São Paulo")
print("b) Brasília")
print("c) Rio de Janeiro")
resposta1 = input("Sua resposta: ").lower()

if resposta1 == "b" or resposta1 == "brasília" or resposta1 == "brasilia":
    print("✅ Correto! Brasília é a capital do Brasil.")
    pontos += 1
else:
    print("❌ Errado. A resposta correta é Brasília.")

print("-" * 40)

# Pergunta 2
print("\n2) Quanto é 5 + 7?")
print("a) 10")
print("b) 11")
print("c) 12")
resposta2 = input("Sua resposta: ").lower()

if resposta2 == "c" or resposta2 == "12":
    print("✅ Correto! 5 + 7 = 12.")
    pontos += 1
else:
    print("❌ Errado. A resposta correta é 12.")

print("-" * 40)

# Pergunta 3
print("\n3) Qual linguagem de programação estamos usando?")
print("a) Java")
print("b) Python")
print("c) C++")
resposta3 = input("Sua resposta: ").lower()

if resposta3 == "b" or resposta3 == "python":
    print("✅ Correto! Estamos usando Python 🐍.")
    pontos += 1
else:
    print("❌ Errado. A resposta correta é Python.")

print("-" * 40)

# Resultado final
print(f"\n {nome}, você terminou o quiz!")
print(f"Pontuação final: {pontos} de 3 pontos possíveis.\n")

if pontos == 3:
    print(" Excelente! Você acertou todas!")
elif pontos == 2:
    print(" Muito bom! Só errou uma.")
elif pontos == 1:
    print(" Você acertou uma, continue praticando!")
else:
    print(" Não acertou nenhuma, mas não desanime. Bora treinar!")
