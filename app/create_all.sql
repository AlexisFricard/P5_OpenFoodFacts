CREATE DATABASE Alimentation;

CREATE USER 'USER_A'@'localhost' IDENTIFIED BY 'USER_A';
GRANT ALL PRIVILEGES ON Alimentation. * TO 'USER_A'@'localhost';

USE Alimentation;

DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Substitute;

CREATE TABLE Category (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(75) NOT NULL UNIQUE,
    PRIMARY KEY (id)
)
ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE Product (
    id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_name CHAR(150) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    category_id SMALLINT UNSIGNED NULL,
    nutriscore CHAR(1) NOT NULL,
    stores VARCHAR(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
    url TEXT NOT NULL,
    PRIMARY KEY (id)
)

ENGINE=INNODB DEFAULT CHARSET=latin1;

CREATE TABLE Substitute (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_id SMALLINT UNSIGNED,
    substituted_id int(200) UNSIGNED,
    PRIMARY KEY (id)
)
ENGINE=INNODB;