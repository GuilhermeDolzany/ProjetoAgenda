import os
import csv

AGENDA = {}


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        save_files()
        print(f"\n>>>>>>> Contato {contato} excluído com sucesso")
    except KeyError:
        print(f"\nNão há {contato} na Agenda")


def buscar_contato(nome):
    contato_dados = AGENDA.get(nome)
    if contato_dados:
        print(f"\nNome: {nome}")
        print(f"Telefone: {contato_dados['telefone']}")
        print(f"Email: {contato_dados['email']}")
        print(f"Endereço: {contato_dados['endereco']}")
        print("\n" + "-" * 30)
    else:
        print("\nContato não encontrado!")


def incluir_editar_contato(contato, telefone, email, endereco, salvar=True):
    status = "editado" if contato in AGENDA else "adicionado"

    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }

    if salvar:
        save_files()
        print(f"\n>>>> Contato {contato} {status} com sucesso!")


def exportar_contatos(file_name):
    try:
        # newline='' é necessário para evitar linhas em branco no Windows
        with open(file_name, "w", encoding="utf-8", newline='') as file:
            escritor = csv.writer(file)
            escritor.writerow(["Nome", "Telefone", "Email", "Endereco"])  # Cabeçalho

            for contato, dados in AGENDA.items():
                escritor.writerow([contato, dados['telefone'], dados['email'], dados['endereco']])
        print(f"\n>>>> Agenda exportada para {file_name} com sucesso!")
    except Exception as error:
        print(f'\n[!] Erro ao exportar contatos: {error}')


def importar_contatos(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            leitor = csv.reader(file)
            header = next(leitor)  # Pula a linha de cabeçalho

            contagem = 0
            for linha in leitor:
                if len(linha) == 4:
                    nome, tel, email, end = linha
                    # salvar=False para não abrir o arquivo físico a cada linha
                    incluir_editar_contato(nome, tel, email, end, salvar=False)
                    contagem += 1

            save_files()  # Salva tudo no banco oficial uma única vez
            print(f"\n>>>> {contagem} contatos importados com sucesso!")
    except FileNotFoundError:
        print("\n[!] Arquivo de importação não encontrado.")
    except Exception as error:
        print(f"\n[!] Erro inesperado ao importar: {error}")


def ler_detalhes_contato():
    telefone = input("Digite o número do telefone: ")
    email = input("Digite o endereço de email: ")
    endereco = input("Digite o endereço: ")
    return telefone, email, endereco


def imprimir_menu():
    print("\n--- MENU AGENDA ---")
    print('1 - Mostrar todos | 2 - Buscar  | 3 - Incluir')
    print('4 - Editar        | 5 - Excluir | 6 - Exportar CSV')
    print('7 - Importar CSV  | 0 - Sair')


def save_files():
    exportar_contatos_silencioso("database.csv")


def exportar_contatos_silencioso(file_name):
    try:
        with open(file_name, "w", encoding="utf-8", newline='') as file:
            escritor = csv.writer(file)
            escritor.writerow(["Nome", "Telefone", "Email", "Endereco"])
            for contato, dados in AGENDA.items():
                escritor.writerow([contato, dados['telefone'], dados['email'], dados['endereco']])
    except:
        pass


def load():
    if os.path.exists("database.csv"):
        importar_contatos_silencioso("database.csv")


def importar_contatos_silencioso(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            leitor = csv.reader(file)
            next(leitor)
            for linha in leitor:
                if len(linha) == 4:
                    nome, tel, email, end = linha
                    AGENDA[nome] = {"telefone": tel, "email": email, "endereco": end}
    except:
        pass


load()
while True:
    imprimir_menu()
    opcao = input('\nEscolha uma opção: ')

    if opcao == '0':
        print("Até a próxima...")
        break

    elif opcao == '1':
        if not AGENDA:
            print("\n[!] A agenda está vazia.")
        else:
            print('-' * 30)
            for nome in AGENDA:
                buscar_contato(nome)

    elif opcao == '2':
        nome = input("Nome para busca: ")
        buscar_contato(nome)

    elif opcao == '3':
        nome = input("Nome: ")
        if nome in AGENDA:
            print(">>>> Contato já existente! Use a opção 4 para editar.")
        else:
            tel, email, end = ler_detalhes_contato()
            incluir_editar_contato(nome, tel, email, end)

    elif opcao == '4':
        nome = input("Nome do contato que deseja editar: ")
        if nome in AGENDA:
            tel, email, end = ler_detalhes_contato()
            incluir_editar_contato(nome, tel, email, end)
        else:
            print(">>>> Contato não encontrado!")

    elif opcao == '5':
        nome = input("Nome para excluir: ")
        excluir_contato(nome)

    elif opcao == '6':
        arquivo = input('Digite o nome do arquivo para exportar (ex: contatos.csv): ')
        exportar_contatos(arquivo)

    elif opcao == '7':
        arquivo = input('Digite o nome do arquivo para importar: ')
        importar_contatos(arquivo)

    else:
        print("Opção inválida!")