CREATE TABLE prontuario (
	id_prontuario INT PRIMARY KEY AUTO_INCREMENT,
	observacoes TEXT NOT NULL,
    id_paciente INT NOT NULL,
	FOREIGN KEY (id_paciente) REFERENCES paciente (id_paciente)
);