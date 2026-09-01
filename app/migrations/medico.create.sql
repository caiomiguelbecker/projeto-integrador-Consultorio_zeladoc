CREATE TABLE medico (
    id_medico INT PRIMARY KEY AUTO_INCREMENT,
    nome_medico VARCHAR(100) NOT NULL,
    id_especialidade INT NOT NULL,
    id_usuario INT NOT NULL,
    FOREIGN KEY (id_especialidade) REFERENCES especialidades(id_especialidade),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);