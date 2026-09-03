CREATE TABLE consulta_exame (
	id_exame INT NOT NULL,
    id_consulta INT NOT NULL,
	FOREIGN KEY (id_exame) REFERENCES exame(id_exame),
	FOREIGN KEY (id_consulta) REFERENCES consulta(id_consulta)
);