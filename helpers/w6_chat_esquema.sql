-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema w6_chat
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema w6_chat
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `w6_chat` ;
USE `w6_chat` ;

-- -----------------------------------------------------
-- Table `w6_chat`.`Chat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `w6_chat`.`Chat` (
  `idchat` INT NOT NULL AUTO_INCREMENT,
  `chat_name` VARCHAR(45) NOT NULL,
  `mssg_id` INT NOT NULL,
  PRIMARY KEY (`idchat`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `w6_chat`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `w6_chat`.`User` (
  `idUser` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUser`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `w6_chat`.`Messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `w6_chat`.`Messages` (
  `idMessages` INT NOT NULL AUTO_INCREMENT,
  `messages_content` VARCHAR(500) NULL,
  `User_idUser` INT NOT NULL,
  `Chat_idchat` INT NOT NULL,
  PRIMARY KEY (`idMessages`),
  INDEX `fk_Messages_User1_idx` (`User_idUser` ASC) VISIBLE,
  INDEX `fk_Messages_Chat1_idx` (`Chat_idchat` ASC) VISIBLE,
  CONSTRAINT `fk_Messages_User1`
    FOREIGN KEY (`User_idUser`)
    REFERENCES `w6_chat`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Messages_Chat1`
    FOREIGN KEY (`Chat_idchat`)
    REFERENCES `w6_chat`.`Chat` (`idchat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `w6_chat`.`Chat_has_User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `w6_chat`.`Chat_has_User` (
  `Chat_idchat` INT NOT NULL,
  `User_idUser` INT NOT NULL,
  PRIMARY KEY (`Chat_idchat`, `User_idUser`),
  INDEX `fk_Chat_has_User_User1_idx` (`User_idUser` ASC) VISIBLE,
  INDEX `fk_Chat_has_User_Chat1_idx` (`Chat_idchat` ASC) VISIBLE,
  CONSTRAINT `fk_Chat_has_User_Chat1`
    FOREIGN KEY (`Chat_idchat`)
    REFERENCES `w6_chat`.`Chat` (`idchat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Chat_has_User_User1`
    FOREIGN KEY (`User_idUser`)
    REFERENCES `w6_chat`.`User` (`idUser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
