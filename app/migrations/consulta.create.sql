CREATE TABLE consulta (
	id_consulta INT PRIMARY KEY AUTO_INCREMENT,
	data_hora DATETIME NOT NULL,
    id_medico INT NOT NULL,
    FOREIGN KEY (id_medico) REFERENCES medico (id_medico)
);


