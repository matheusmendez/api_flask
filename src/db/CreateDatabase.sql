USE db_carros;

CREATE TABLE tb_carros (
	id INTEGER NOT NULL AUTO_INCREMENT,
	marca VARCHAR(100),
	modelo VARCHAR(100),
	ano INTEGER,
	PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;


INSERT INTO tb_carros (marca, modelo, ano) VALUES ('Fiat',  'Marea', 1999);
INSERT INTO tb_carros (marca, modelo, ano) VALUES ('Fiat',  'Uno', 1992);
INSERT INTO tb_carros (marca, modelo, ano) VALUES ('Ford',  'Escort', 1985);
INSERT INTO tb_carros (marca, modelo, ano) VALUES ('Chevrolet',  'Chevette', 1978);
INSERT INTO tb_carros (marca, modelo, ano) VALUES ('Volkswagen',  'Fusca', 1962);
