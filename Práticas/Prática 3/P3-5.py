names = [""]
while names[-1] != "exit":
    names.append(input("Insere um nome ou escreve \"exit\" para sair: "))
for name in names[1:-1]:
    print(name)