ALTER TABLE consulta 
ADD COLUMN id_paciente INT NOT NULL,
ADD FOREIGN KEY (id_paciente) REFERENCES paciente(id_paciente);