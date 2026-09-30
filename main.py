alunos = {}


def menu_home():
    print("1. Adicionar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno pelo nome")
    print("4. Remover aluno")
    print("5. Mostrar média geral das notas da turma")
    print("6. Sair")
    
def listar_alunos():
    print("Lista de todos os alunos:")
    for nome, nota in alunos.items():
        print(f"Nome: {nome}, Nota: {nota}")

def add_aluno():
    print("informe o nome do aluno a ser adicionado e nota")
    alunos_add = input("digite o nome do aluno ")
    if alunos_add in alunos:
        print("aluno já cadastrado")
    else:
        print("Adicionar aluno e nota")
        notas_add = float(input("digite a nota"))
        alunos[alunos_add] = notas_add
        print("aluno add com sucesso")

def buscar_nome():
    print("Informe o nome do aluno a ser buscado")
    
    while True:
        nome_busca = input("Digite o nome do aluno: ")
    
        if nome_busca in alunos:
            print("Aluno encontrado")
            print(f"nota do a aluno é {alunos[nome_busca]}")

        else:
            print("Aluno nao encontrado")
        
        continuar = input("Deseja buscar outro aluno? (s/n): ")
        if continuar != 's':
            break

def remover_aluno():
    print("Informe o nome do aluno a ser removido")
    nome_remove = input("Digite o nome do aluno: ")
    if nome_remove in alunos:
        del alunos[nome_remove]
        print("Aluno removido com sucesso")
    else:
        print("Aluno não encontrado")

def media_geral():
    print("Média dos alunos")
    if not alunos:
        print("nenhum aluno cadastrado")
        return

    soma = 0
    for nota in alunos.values():
        soma = soma + nota
    
    media = soma / len(alunos)
    print(f"A media geral da turma é: {media:.2f}")

def sair():
    print("Saindo do programa...")
    exit()
        
def main():
    while True:
        menu_home()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            add_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_nome()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            media_geral()
        elif opcao == '6':
            sair()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
