ALTER TABLE paciente
ADD COLUMN id_convenio INT,
ADD FOREIGN KEY (id_convenio) REFERENCES convenio(id_convenio);