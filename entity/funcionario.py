class Funcionario:
    
    def __init__(self,nome,sexo,cpf,email,telefone,data_nascimento,departamento,cargo):
        self.__nome = nome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__data_nascimento = data_nascimento
        self.__departamento = departamento
        self.__cargo = cargo

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self,sexo):
        self.__sexo = sexo
        
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email): 
        self.__email = email
    
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self,departamento):
        self.__departamento = departamento
        
    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self,cargo):
        self.__cargo = cargo
    
    
    def __str__(self):
        return f"""
NOME: {self.__nome}
SEXO: {self.__sexo}
CPF: {self.__cpf}
EMAIL: {self.__email}
TELEFONE: {self.__telefone}
DATA NASCIMENTO: {self.__data_nascimento}
DEPARTAMENTO: {self.__departamento}
CARGO: {self.__cargo}
"""