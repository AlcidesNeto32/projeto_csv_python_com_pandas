from datetime import datetime as dt
import csv,re, pandas as pd

path = "/home/alcides-neto/Documents/EstudandoCobraLaele/funcionarios/funcionarios.csv"
class FuncionarioService:

    def cadastrar_funcionario(self,Funcionario):
         if len(Funcionario.nome) < 10:
             return "NOME INVÁLIDO!"
         if not self.validate_cpf(cpf=Funcionario.cpf):
             return 'CPF INVÁLIDO!'
         if not Funcionario.telefone.isdigit() or len(Funcionario.telefone) != 9:
             return 'TELEFONE INVÁLIDO!'
         if Funcionario.data_nascimento.year > dt.now().year:
             return "DATA INVÁLIDA!"
         if dt.now().year - Funcionario.data_nascimento.year < 18:
             return "O CANDIDATO DEVE SER MAIOR DE IDADE!"
         if not self.validate_email(Funcionario.email):
             return "EMAIL INVÁLIDO!"
         if Funcionario.sexo != "M" and Funcionario.sexo != "F":
             return "SEXO INVÁLIDO!"
         if self.busca_funcionario(Funcionario.cpf) == "Funcionário não encontrado":
             return "CPF JÁ CADASTRADO EM NOSSO SISTEMA!"


         with open(path,"a",newline="") as func_file:
             campos = ["nome","sexo","cpf","email","telefone","data_nascimento","departamento","cargo"]
             preencher_file = csv.DictWriter(func_file,fieldnames=campos)
             preencher_file.writer(
                     {"nome":Funcionario.nome,
                     "sexo":Funcionario.sexo,
                     "cpf":Funcionario.cpf,
                     "email":Funcionario.email,
                     "telefone":Funcionario.telefone,
                     "data_nascimento":Funcionario.data_nascimento,
                     "departamento":Funcionario.departamento,
                     "cargo":Funcionario.cargo,
                     })
         return "Funcionário(a) cadastrado com sucesso!"
    
    def relatorio_geral(self):
        funcionarios = pd.read_csv(path)
        funcionarios["data_nascimento"] = pd.to_datetime(funcionarios["data_nascimento"])
        funcionarios["idade"] = dt.now().year - funcionarios["data_nascimento"].dt.year
        print(f"""
TOTAL DE DEPARTAMENTOS: {funcionarios["departamento"].value_counts().count()}
TOTAL DE FUNCIONARIOS: {funcionarios["cpf"].count()} 
TOTAL DE FUNCIONARIOS POR DEPARTAMENTO: 
{funcionarios["departamento"].value_counts()}
MÉDIA DE IDADE DOS FUNCIONARIOS: {round(funcionarios['idade'].mean(),0)}
QUANTIDADE DE FUNCIONÁRIOS POR SEXO: 
{funcionarios["sexo"].value_counts()}
""")        
    def busca_funcionario(self,cpf):
        if not self.validate_cpf(cpf):
            return("CPF INVÁLIDO!")
                    
        with open(path,"r") as func_file:
            funcionarios_dict = csv.DictReader(func_file)
            for funcionario in funcionarios_dict:
                if funcionario['cpf'] == cpf:
                            return f"""
NOME: {funcionario['nome']}
SEXO: {funcionario['sexo']}
CPF: {funcionario['cpf']}
EMAIL: {funcionario['email']}
TELEFONE: {funcionario['telefone']}
DATA NASCIMENTO: {funcionario['data_nascimento']}
DEPARTAMENTO: {funcionario['departamento']}
CARGO: {funcionario['cargo']}
"""
        return "Funcionário(a) não encontrado"
    
    def atualizar_dados_funcionario(self,nome,sexo,cpf,email,telefone,departamento,cargo):
        
       with open(path,"r") as func_file:
            funcionarios = list(csv.DictReader(func_file))
            
       for funcionario in funcionarios:
           if funcionario['cpf'] == cpf:
               funcionario.update({
                   'nome':nome,'sexo':sexo,
                   'email':email,'telefone':telefone,
                   'departamento':departamento,'cargo':cargo})
               break
       with open(path,"w") as func_file:
            cabecalho = ['nome','sexo','cpf','email','telefone','data_nascimento','departamento','cargo']
            writer = csv.DictWriter(func_file,fieldnames=cabecalho)
            writer.writeheader()
            writer.writerows(funcionarios)
   
    @staticmethod
    def listar_funcionarios():
        with open(path,"r") as func_csv:
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
            
    #validação simples
    def validate_email(self,email):
        regex_email = "^\S+@\S+\.\S+$"
        return re.match(regex_email,email)
        
        
    def validate_cpf(self,cpf: str) -> bool:

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
