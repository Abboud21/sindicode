CREATE DATABASE IF NOT EXISTS sindcode;
USE sindcode;
SELECT * FROM noticia;

DROP TABLE IF EXISTS noticia;
CREATE TABLE IF NOT EXISTS autor(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(80) NOT NULL,
    perfil TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS categoria(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS noticia(
	id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(90) NOT NULL,
    conteudo TEXT NOT NULL,
    data_publicacao DATETIME NOT NULL,
    destaque ENUM('0','1','2','3','4') NOT NULL DEFAULT '0',
    foto VARCHAR(60) NOT NULL,
    id_autor INT NOT NULL,
    id_categoria INT NOT NULL,
    
    CONSTRAINT fk_noticia_autor
		FOREIGN KEY (id_autor) REFERENCES autor(id),
	CONSTRAINT fk_noticia_categoria
		FOREIGN KEY (id_categoria) REFERENCES categoria(id)
);