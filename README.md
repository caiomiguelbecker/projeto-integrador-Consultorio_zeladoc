# 🩺 ZelaDoc — Sistema de Gestão para Consultório Médico

Projeto Integrador do curso Técnico em Desenvolvimento de Sistemas.

O ZelaDoc é um sistema desktop (mini ERP) em Python para a gestão de um consultório médico. Permite cadastrar pacientes, médicos, especialidades, convênios, exames, consultas e prontuários, com acesso protegido por login.

---

## ✅ Funcionalidades

- Login com senha protegida por hash (SHA-256 + salt)
- Cadastro, consulta, alteração e exclusão (CRUD) de:
  - Pacientes (com endereço e convênio)
  - Médicos (com CRM e especialidade)
  - Especialidades, Convênios e Exames
  - Consultas (paciente, médico, data/hora e exames solicitados)
  - Prontuários
  - Usuários do sistema

---

## 🛠️ Tecnologias

- **Python 3.10+**
- **MySQL** (banco de dados)
- **Tkinter + ttkbootstrap** (interface gráfica)
- Bibliotecas: `mysql-connector-python`, `ttkbootstrap`, `python-dotenv`, `pillow`, `pywinstyles`

> O sistema foi desenvolvido e testado no **Windows 11**.

---

## 🚀 Como executar o projeto

### 1. Pré-requisitos

- Python 3.10 ou superior instalado
- MySQL Server instalado e rodando (ex.: MySQL Workbench)

### 2. Baixar o projeto

```bash
git clone https://github.com/caiomiguelbecker/projeto-integrador-Consultorio_zeladoc.git
cd projeto-integrador-Consultorio_zeladoc
```

Ou clique em **Code → Download ZIP** e extraia a pasta.

### 3. Criar o ambiente virtual e instalar as dependências

No terminal (PowerShell), dentro da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> Se estiver usando o **Prompt de Comando (CMD)**, ative o ambiente com `.venv\Scripts\activate`.

> ⚠️ **Caso ocorra um erro de segurança** informando que a execução de scripts está desabilitada no sistema, execute o comando abaixo e tente ativar o ambiente novamente:
>
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
>
> Em computadores com permissões restritas (como os da instituição), se o comando acima não for permitido, use a opção temporária, válida apenas para o terminal aberto:
>
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
> ```

### 4. Criar o banco de dados

Abra o arquivo **`zeladoc_banco.sql`** (na raiz do projeto) no MySQL Workbench e execute-o por inteiro (ícone do raio ⚡).
Ele cria o banco `zeladoc` e todas as tabelas já na ordem correta.

> A pasta `app/migrations` guarda o histórico dos scripts criados durante o desenvolvimento. Não é necessário executá-los: o `zeladoc_banco.sql` já contém tudo.

### 5. Configurar a conexão com o banco

Copie o arquivo `.env.example`, renomeie a cópia para **`.env`** e preencha com os dados do seu MySQL:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha_aqui
DB_NAME=zeladoc
```

> ⚠️ **Atenção ao nome do arquivo:** ao baixar o projeto, o Windows pode remover o ponto do início e o arquivo aparecer como `env.example` ou `env`. O nome precisa começar com ponto, senão o sistema não encontra a configuração do banco. Para corrigir no **VS Code**:
>
>
> 1. Renomeie o nome exatamente assim no começo: **`.env`** (com o ponto no começo e sem `.txt` no final) após efetuar o download.
> 2. Confirme que o arquivo `.env` está na **raiz do projeto**, na mesma pasta do `main.py`.
> 3. Salve e abra o `.env`, preencha a senha do seu MySQL e salve novamente (`Ctrl + S`).
>
> O arquivo `.env` deve ficar na **raiz do projeto**, na mesma pasta do `main.py`.

### 6. Criar o usuário administrador

```bash
python seed_admin.py
```

Informe nome, e-mail e senha. Esses dados serão usados no login.

### 7. Iniciar o sistema

```bash
python main.py
```

---

## 📁 Estrutura do projeto

```
├── app/
│   ├── models/        # Entidades do sistema e regras de validação
│   ├── views/         # Telas (Tkinter/ttkbootstrap)
│   ├── controller/    # Ligação entre as telas e os dados
│   ├── dao/           # Acesso ao banco MySQL (SQL)
│   ├── core/          # Utilitários (conexão, senha, datas, textos)
│   └── migrations/    # Histórico dos scripts SQL
├── assets/            # Ícone e logos
├── main.py            # Ponto de entrada do sistema
├── seed_admin.py      # Cria o primeiro usuário administrador
├── zeladoc_banco.sql  # Script completo do banco de dados
├── requirements.txt   # Dependências do projeto
└── .env.example       # Modelo de configuração do banco
```

---

## 🏛️ Arquitetura

O projeto segue o padrão **MVC (Model-View-Controller)** com uma camada extra de **DAO**:

**View** (tela) → **Controller** (valida e monta os objetos) → **DAO** (executa o SQL) → **MySQL**

- **Models:** representam as entidades e validam seus dados.
- **Views:** cuidam apenas da interface, sem regra de negócio.
- **Controllers:** recebem os dados da tela, validam e chamam os DAOs.
- **DAO:** isola todo o acesso ao banco; todos herdam de uma classe abstrata com `save`, `get_all`, `get_by_id`, `update` e `delete`.

---

## 👥 Equipe

- Caio Miguel
- Pedro Zagar
- Rogério Quaresma Mastella
