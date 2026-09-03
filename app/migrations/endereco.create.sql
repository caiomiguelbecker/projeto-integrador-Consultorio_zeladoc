CREATE TABLE endereco (
	id_endereco INT PRIMARY KEY AUTO_INCREMENT,
	logradouro TEXT NOT NULL,
	numero INT NOT NULL,
	cidade VARCHAR(100) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    id_paciente INT NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES paciente(id_paciente)
);