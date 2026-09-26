-- ============================================================
-- ZelaDoc - Banco de dados (MySQL)
-- 1: Criar o banco e todas as tabelas (Estão na ordem correta).
-- 2: Executar o arquivo inteiro.
-- 3: Enjoy :).
-- ============================================================

CREATE DATABASE IF NOT EXISTS zeladoc
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE zeladoc;

-- ------------------------------------------------------------
-- 1) Tabelas base (não dependem de nenhuma outra)
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS convenio (
    id_convenio INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS especialidades (
    id_especialidade INT PRIMARY KEY AUTO_INCREMENT,
    nome_especialidade VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS exame (
    id_exame INT PRIMARY KEY AUTO_INCREMENT,
    nome_exame VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS usuario (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome_usuario VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL
);

-- ------------------------------------------------------------
-- 2) Tabelas que dependem das tabelas base
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS paciente (
    id_paciente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    id_convenio INT,
    FOREIGN KEY (id_convenio) REFERENCES convenio (id_convenio)
);

CREATE TABLE IF NOT EXISTS medico (
    id_medico INT PRIMARY KEY AUTO_INCREMENT,
    nome_medico VARCHAR(100) NOT NULL,
    crm VARCHAR(20) NOT NULL,
    id_especialidade INT NOT NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_especialidade) REFERENCES especialidades (id_especialidade),
    FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
);

-- ------------------------------------------------------------
-- 3) Tabelas que dependem de paciente e/ou médico
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS endereco (
    id_endereco INT PRIMARY KEY AUTO_INCREMENT,
    logradouro TEXT NOT NULL,
    numero INT NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    id_paciente INT NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES paciente (id_paciente)
);

CREATE TABLE IF NOT EXISTS prontuario (
    id_prontuario INT PRIMARY KEY AUTO_INCREMENT,
    observacoes TEXT NOT NULL,
    id_paciente INT NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES paciente (id_paciente)
);

CREATE TABLE IF NOT EXISTS consulta (
    id_consulta INT PRIMARY KEY AUTO_INCREMENT,
    data_hora DATETIME NOT NULL,
    id_medico INT NOT NULL,
    id_paciente INT NOT NULL,
    FOREIGN KEY (id_medico) REFERENCES medico (id_medico),
    FOREIGN KEY (id_paciente) REFERENCES paciente (id_paciente)
);

-- ------------------------------------------------------------
-- 4) Tabela de ligação (muitos-para-muitos entre consulta e exame)
-- ------------------------------------------------------------

CREATE TABLE IF NOT EXISTS consulta_exame (
    id_exame INT NOT NULL,
    id_consulta INT NOT NULL,
    FOREIGN KEY (id_exame) REFERENCES exame (id_exame),
    FOREIGN KEY (id_consulta) REFERENCES consulta (id_consulta)
);