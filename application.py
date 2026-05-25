from datetime import datetime as dt
import time
from entity import funcionario 
from service import funcionario_service

menu = """
---------------------------------------------
MENU
---------------------------------------------
1.CADASTRAR FUNCIONÁRIO
2.PESQUISAR FUNCIONÁRIO
3.ATUALIZAR DADOS DO FUNCIONÁRIO
4.LISTAR FUNCIONÁRIOS
5.EMITIR RELATÓRIO GERAL
6.SAIR

SELECIONE A OPÇÃO:
"""


funcionario_service = funcionario_service.FuncionarioService()
while True:
    opcao = int(input(menu))
    try:
        match opcao:
            case 1:
                nome = input("NOME: ")
                sexo = input("SEXO M/F: ")
                cpf = input("CPF: ")
                email = input("EMAIL: ")
                telefone = input("TELEFONE: ")
                departamento = input("DEPARTAMENTO: ")
                cargo = input("CARGO: ")
                try:
                    data_nascimento = dt.strptime(input("DATA DE NASCIMENTO (DD/MM/AAAA): "),'%d/%m/%Y').date()
                    print("Verificando informações",end="",flush=True)
                    for i in range(3):
                        print(".",end="",flush=True)
                        time.sleep(0.5)
                    print()
                    novo_funcionario = funcionario.Funcionario(nome,sexo,cpf,email,telefone,data_nascimento,departamento,cargo)
                    print(funcionario_service.cadastrar_funcionario(novo_funcionario))
                except ValueError:
                    print("Data inválida!")
            case 2:
                cpf = input("Digite o CPF do funcionário: ")
                resultado = funcionario_service.busca_funcionario(cpf)
                print(resultado)
            case 3:
                nome = input("NOME: ")
                sexo = input("SEXO: ")
                cpf = input("CPF: ")
                email = input("EMAIL: ")
                telefone = input("TELEFONE: ")
                departamento = input("DEPARTAMENTO: ")
                cargo = input("CARGO: ")
                print("Atualizando",end="",flush=True)
                for i in range(3):
                    print(".",end="",flush=True)
                    time.sleep(0.5)
                print()
                print(funcionario_service.atualizar_dados_funcionario(nome,sexo,cpf,email,telefone,departamento,cargo))
            case 4:
                funcionario_service.listar_funcionarios()
            case 5:
                funcionario_service.relatorio_geral()
            case 6:

                print("Saindo",end="",flush=True)
                for i in range(3):
                    print(".",end="",flush=True)
                    time.sleep(0.5)
                break
            case _:
                print("Essa opção não existe!")
    except ValueError:
        print("Digite o valor da opção correspondente!")