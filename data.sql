CREATE TABLE `cursos` (
  `codigo` INT(10) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `creditos` INT(10) NULL,
  PRIMARY KEY(`codigo`)
) engine=InnoDB DEFAULT CHARSET utf8 COLLATE utf8_spanish_ci