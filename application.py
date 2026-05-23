from datetime import datetime as dt
import csv,re,time,pandas as pd
from entity import funcionario

class FuncionarioService:
    
    def cadastrar_funcionario(self,Funcionario):
         if len(Funcionario.nome) < 10:
             return "NOME INVÁLIDO!"
         if not validate_cpf(cpf=Funcionario.cpf):
             return 'CPF INVÁLIDO!'
         if not Funcionario.telefone.isdigit() or len(Funcionario.telefone) != 9:
             return 'TELEFONE INVÁLIDO!'
         if Funcionario.data_nascimento.year > dt.now().year:
             return "DATA INVÁLIDA!"
         if dt.now().year - Funcionario.data_nascimento.year < 18:
             return "O CANDIDATO DEVE SER MAIOR DE IDADE!"
         if not validate_email(Funcionario.email):
             return "EMAIL INVÁLIDO!"
         if Funcionario.sexo != "M" and Funcionario.sexo != "F":
             return "SEXO INVÁLIDO!"
         if self.busca_funcionario(Funcionario.cpf) == "Funcionário não encontrado":
             return "CPF JÁ CADASTRADO EM NOSSO SISTEMA!"

         dados_func = {"nome":Funcionario.nome,
                     "sexo":Funcionario.sexo,
                     "cpf":Funcionario.cpf,
                     "email":Funcionario.email,
                     "telefone":Funcionario.telefone,
                     "data_nascimento":Funcionario.data_nascimento,
                     "departamento":Funcionario.departamento,
                     "cargo":Funcionario.cargo,
                     }

         with open("/home/alcides-neto/Documents/EstudandoCobraLaele/funcionarios/funcionarios.csv","a",newline="") as func_file:
             campos = ["nome","sexo","cpf","email","telefone","data_nascimento","departamento","cargo"]
             preencher_file = csv.DictWriter(func_file,fieldnames=campos)
             preencher_file.writerow(
                 {"nome":dados_func['nome'],
                 "sexo":dados_func['sexo'],
                 "cpf":dados_func['cpf'],
                 "email":dados_func['email'],
                 "telefone":dados_func['telefone'],
                 "data_nascimento":dados_func['data_nascimento'],
                 "departamento":dados_func['departamento'],
                 "cargo":dados_func['cargo']}
                                     )
         return "Funcionário(a) cadastrado com sucesso!"
    
    def busca_funcionario(self,cpf):
        if not validate_cpf(cpf):
            return("CPF INVÁLIDO!")
                    
        with open("/home/alcides-neto/Documents/EstudandoCobraLaele/funcionarios/funcionarios.csv","r") as func_file:
            funcionarios_dict = csv.DictReader(func_file)
            for funcionario in funcionarios_dict:
                if funcionario['cpf'] == cpf:
                            return f"""
    NOME: {funcionario['nome']}
    SEXO: {funcionario['sexo']}
    CPF: {funcionario['cpf']}
    DATA NASCIMENTO: {funcionario['data_nascimento']}
    DEPARTAMENTO: {funcionario['departamento']}
    CARGO: {funcionario['cargo']}"""
        return "Funcionário(a) não encontrado"
    
    def atualizar_dados_funcionario(self,nome,sexo,cpf,email,telefone,departamento,cargo):
        
       with open("/home/alcides-neto/Documents/EstudandoCobraLaele/funcionarios/funcionarios.csv","r") as func_file:
            funcionarios = list(csv.DictReader(func_file))
            
       for funcionario in funcionarios:
           if funcionario['cpf'] == cpf:
               funcionario.update({
                   'nome':nome,'sexo':sexo,
                   'email':email,'telefone':telefone,
                   'departamento':departamento,'cargo':cargo})
               break
       with open("/home/alcides-neto/Documents/EstudandoCobraLaele/funcionarios/funcionarios.csv","w") as func_file:
            cabecalho = ['nome','sexo','cpf','email','telefone','data_nascimento','departamento','cargo']
            writer = csv.DictWriter(func_file,fieldnames=cabecalho)
            writer.writeheader()
            writer.writerows(funcionarios)
   
    @staticmethod
    def listar_funcionarios():
        with open("/home/alcides-neto/Documents/EstudandoCobraLaele/funcionarios/funcionarios.csv","r") as func_csv:
            dict_funcionarios = list(csv.DictReader(func_csv))
        
        if len(dict_funcionarios) == 0:
            print("Não há funcionários cadastrados.")
            return
        
        for funcionario in dict_funcionarios:
            print(f"""
NOME: {funcionario['nome']}
SEXO: {funcionario['sexo']}
CPF: {funcionario['cpf']}
EMAIL: {funcionario['email']}
TELEFONE: {funcionario['telefone']}
DATA NASCIMENTO: {funcionario['data_nascimento']}
DEPARTAMENTO: {funcionario['departamento']}
CARGO: {funcionario['cargo']}
""")

       
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

def relatorio_geral():
        funcionarios = pd.read_csv("/home/alcides-neto/Documents/EstudandoCobraLaele/funcionarios/funcionarios.csv")
        print(funcionarios.departamento)
                    
#validação simples
def validate_email(email):
    regex_email = "^\S+@\S+\.\S+$"
    return re.match(regex_email,email)
    
    
def validate_cpf(cpf: str) -> bool:

    # Verifica a formatação do CPF
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
        return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True


while True:
    opcao = int(input(menu))
    funcionario_service = FuncionarioService()
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
                funcionario = funcionario_service.busca_funcionario(cpf)
                print(funcionario)
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
                relatorio_geral()
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

