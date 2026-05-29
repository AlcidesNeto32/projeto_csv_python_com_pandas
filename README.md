# 🗂️ Sistema de Gestão de Funcionários — Python + Pandas

Sistema de cadastro e gerenciamento de funcionários via terminal, com persistência em arquivo CSV e geração de relatórios com Pandas.

---

## 📋 Sobre o Projeto

Esta aplicação permite gerenciar um cadastro de funcionários diretamente pelo terminal. Os dados são armazenados em um arquivo `.csv` e o sistema conta com validações robustas de entrada, além de um módulo de relatório utilizando a biblioteca **Pandas**.

---

## ✨ Funcionalidades

- ✅ **Cadastrar funcionário** — com validação de nome, CPF, telefone, e-mail, data de nascimento, sexo e maioridade
- 🔍 **Pesquisar funcionário** — busca por CPF
- ✏️ **Atualizar dados** — edição dos dados de um funcionário existente
- 📋 **Listar funcionários** — exibe todos os cadastros
- 📊 **Emitir relatório geral** — leitura e exibição dos dados via Pandas

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem principal |
| `csv` | Leitura e escrita do arquivo de dados |
| `pandas` | Geração de relatório geral |
| `re` | Validação de CPF e e-mail via regex |

---

## 📁 Estrutura do Projeto

```
projeto/
├── application.py       # Lógica principal e menu interativo
├── entity/
│   └── funcionario.py   # Classe/modelo Funcionario
│── service/
│   └── funcionario_service.py # Classe de serviço
├── funcionarios.csv     # Arquivo de dados (gerado na primeira execução)
└── .gitignore
```

---

## ▶️ Como Executar

**Pré-requisitos:** Python 3.10+ e Pandas instalados.

```bash
# Instale a dependência
pip install pandas

# Execute a aplicação
python application.py
```

Ao iniciar, o menu interativo será exibido no terminal:

```
---------------------------------------------
MENU
---------------------------------------------
1. CADASTRAR FUNCIONÁRIO
2. PESQUISAR FUNCIONÁRIO
3. ATUALIZAR DADOS DO FUNCIONÁRIO
4. LISTAR FUNCIONÁRIOS
5. EMITIR RELATÓRIO GERAL
6. SAIR
```

---

## ✔️ Validações Implementadas

- **Nome:** mínimo de 10 caracteres
- **CPF:** formato `XXX.XXX.XXX-XX` com validação dos dígitos verificadores
- **Telefone:** apenas dígitos, exatamente 9 caracteres
- **E-mail:** validação via regex
- **Data de nascimento:** não pode ser futura; candidato deve ser maior de 18 anos
- **Sexo:** aceita apenas `M` ou `F`
- **CPF duplicado:** impede o cadastro de um CPF já existente

---

## ⚠️ Observações

> O caminho do arquivo CSV está definido de forma absoluta em `application.py`. Antes de executar, ajuste a constante de caminho para o diretório correto na sua máquina:
>
> ```python
> # Exemplo — altere para o seu caminho
> "/seu/caminho/para/funcionarios.csv"
> ```

---

## 👨‍💻 Autor

**Alcides Neto** — [GitHub](https://github.com/AlcidesNeto32)