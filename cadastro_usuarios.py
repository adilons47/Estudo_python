def verificadordegrupoetario(idade_usuario):
    if idade_usuario >= 60:
        return "Idoso"
    elif idade_usuario >= 18:
        return "Adulto"
    elif idade_usuario >= 13:
        return "Adolescente"
    else:
        return "Criança"

def rg_valido(rg_usuario):
    return len(rg_usuario) == 7 and rg_usuario.isdigit()

nome = input("Informe seu nome: ")
print("Nome registrado com sucesso!")

rg = input("Informe seu RG: ")
while not rg_valido(rg):
    print("RG inválido. Digite exatamente 7 números.")
    rg = input("Informe seu RG: ")
print("RG registrado com sucesso!")

idade = int(input("Informe sua idade: "))
print("Idade registrada com sucesso!")

grupo_etario = verificadordegrupoetario(idade)

print("\nUsuário registrado!\n")
print(f"Nome: {nome}")
print(f"RG: {rg}")
print(f"Grupo etário: {grupo_etario}")
