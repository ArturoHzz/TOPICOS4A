-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dbfarmacia
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dbfarmacia
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dbfarmacia` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `dbfarmacia` ;

-- -----------------------------------------------------
-- Table `dbfarmacia`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`categoria` (
  `idCategoria` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCategoria`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`cliente` (
  `idTelefono` CHAR(10) NOT NULL,
  `Nombres` VARCHAR(100) NOT NULL,
  `Apellidos` VARCHAR(100) NOT NULL,
  `Correo` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idTelefono`),
  INDEX `idx_cliente_apellidos` (`Apellidos` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`proveedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`proveedor` (
  `idProveedor` INT NOT NULL,
  `Nombre` VARCHAR(50) NOT NULL,
  `Telefono` CHAR(10) NOT NULL,
  `Email` VARCHAR(100) NOT NULL,
  `Direccion` VARCHAR(100) NOT NULL,
  `Rfc` CHAR(13) NOT NULL,
  PRIMARY KEY (`idProveedor`),
  INDEX `idx_proveedor_nombre` (`Nombre` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`empleado` (
  `idEmpleado` INT NOT NULL,
  `Nombres` VARCHAR(100) NOT NULL,
  `Apellidos` VARCHAR(100) NOT NULL,
  `RFC` VARCHAR(13) NOT NULL,
  PRIMARY KEY (`idEmpleado`),
  INDEX `idx_empleado_rfc` (`RFC` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`compra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`compra` (
  `idCompra` INT NOT NULL,
  `Fecha` DATE NOT NULL,
  `Total` DECIMAL(10,2) NOT NULL,
  `Observaciones` TEXT NULL DEFAULT NULL,
  `Proveedor_idProveedor` INT NOT NULL,
  `Empleado_idEmpleado` INT NOT NULL,
  PRIMARY KEY (`idCompra`),
  INDEX `Empleado_idEmpleado` (`Empleado_idEmpleado` ASC) VISIBLE,
  INDEX `idx_compra_fecha` (`Fecha` ASC) VISIBLE,
  INDEX `idx_compra_proveedor` (`Proveedor_idProveedor` ASC) VISIBLE,
  CONSTRAINT `compra_ibfk_1`
    FOREIGN KEY (`Proveedor_idProveedor`)
    REFERENCES `dbfarmacia`.`proveedor` (`idProveedor`),
  CONSTRAINT `compra_ibfk_2`
    FOREIGN KEY (`Empleado_idEmpleado`)
    REFERENCES `dbfarmacia`.`empleado` (`idEmpleado`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`unidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`unidad` (
  `idUnidad` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Abreviatura` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idUnidad`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`producto` (
  `idCodigo` CHAR(13) NOT NULL,
  `Nombre` VARCHAR(100) NOT NULL,
  `Contenido` INT NOT NULL,
  `CostoUnitario` DECIMAL(10,2) NOT NULL,
  `PrecioUnitario` DECIMAL(10,2) NOT NULL,
  `Existencia` INT NOT NULL,
  `Activo` TINYINT NOT NULL,
  `Categoria_idCategoria` INT NOT NULL,
  `Unidad_idUnidad` INT NOT NULL,
  PRIMARY KEY (`idCodigo`),
  INDEX `Unidad_idUnidad` (`Unidad_idUnidad` ASC) VISIBLE,
  INDEX `idx_producto_nombre` (`Nombre` ASC) VISIBLE,
  INDEX `idx_producto_categoria` (`Categoria_idCategoria` ASC) VISIBLE,
  CONSTRAINT `producto_ibfk_1`
    FOREIGN KEY (`Categoria_idCategoria`)
    REFERENCES `dbfarmacia`.`categoria` (`idCategoria`),
  CONSTRAINT `producto_ibfk_2`
    FOREIGN KEY (`Unidad_idUnidad`)
    REFERENCES `dbfarmacia`.`unidad` (`idUnidad`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`formapago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`formapago` (
  `idFormaPago` INT NOT NULL,
  `Nombre` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idFormaPago`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`venta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`venta` (
  `idVenta` INT NOT NULL,
  `Fecha_Hora` DATETIME NOT NULL,
  `Descuento` DECIMAL(10,2) NOT NULL,
  `IVA` DECIMAL(10,2) NOT NULL,
  `Total` DECIMAL(10,2) NOT NULL,
  `Empleado_idEmpleado` INT NOT NULL,
  `Cliente_idTelefono` CHAR(10) NOT NULL,
  `FormaPago_idFormaPago` INT NOT NULL,
  PRIMARY KEY (`idVenta`),
  INDEX `FormaPago_idFormaPago` (`FormaPago_idFormaPago` ASC) VISIBLE,
  INDEX `idx_venta_fecha` (`Fecha_Hora` ASC) VISIBLE,
  INDEX `idx_venta_empleado` (`Empleado_idEmpleado` ASC) VISIBLE,
  INDEX `idx_venta_cliente` (`Cliente_idTelefono` ASC) VISIBLE,
  CONSTRAINT `venta_ibfk_1`
    FOREIGN KEY (`Empleado_idEmpleado`)
    REFERENCES `dbfarmacia`.`empleado` (`idEmpleado`),
  CONSTRAINT `venta_ibfk_2`
    FOREIGN KEY (`Cliente_idTelefono`)
    REFERENCES `dbfarmacia`.`cliente` (`idTelefono`),
  CONSTRAINT `venta_ibfk_3`
    FOREIGN KEY (`FormaPago_idFormaPago`)
    REFERENCES `dbfarmacia`.`formapago` (`idFormaPago`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`detalles_venta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`detalles_venta` (
  `idDetalles_Venta` INT NOT NULL,
  `Cantidad` INT NOT NULL,
  `PrecioUnitario` DECIMAL(10,2) NOT NULL,
  `Subtotal` DECIMAL(10,2) NOT NULL,
  `Producto_idCodigo` CHAR(13) NOT NULL,
  `Venta_idVenta` INT NOT NULL,
  PRIMARY KEY (`idDetalles_Venta`),
  INDEX `Venta_idVenta` (`Venta_idVenta` ASC) VISIBLE,
  INDEX `idx_detalles_venta_producto` (`Producto_idCodigo` ASC) VISIBLE,
  CONSTRAINT `detalles_venta_ibfk_1`
    FOREIGN KEY (`Producto_idCodigo`)
    REFERENCES `dbfarmacia`.`producto` (`idCodigo`),
  CONSTRAINT `detalles_venta_ibfk_2`
    FOREIGN KEY (`Venta_idVenta`)
    REFERENCES `dbfarmacia`.`venta` (`idVenta`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`detallescompra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`detallescompra` (
  `idDetallesCompra` INT NOT NULL,
  `Cantidad` DECIMAL(10,2) NOT NULL,
  `CostoUnitario` DECIMAL(10,2) NOT NULL,
  `Compra_idCompra` INT NOT NULL,
  `Producto_idCodigo` CHAR(13) NOT NULL,
  PRIMARY KEY (`idDetallesCompra`),
  INDEX `Compra_idCompra` (`Compra_idCompra` ASC) VISIBLE,
  INDEX `idx_detalles_compra_producto` (`Producto_idCodigo` ASC) VISIBLE,
  CONSTRAINT `detallescompra_ibfk_1`
    FOREIGN KEY (`Compra_idCompra`)
    REFERENCES `dbfarmacia`.`compra` (`idCompra`),
  CONSTRAINT `detallescompra_ibfk_2`
    FOREIGN KEY (`Producto_idCodigo`)
    REFERENCES `dbfarmacia`.`producto` (`idCodigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`entradas_salidas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`entradas_salidas` (
  `idEntradas_Salidas` INT NOT NULL,
  `Movimiento` ENUM('ENTRADA', 'SALIDA') NOT NULL,
  `StockAnterior` INT NOT NULL,
  `StockNuevo` INT NOT NULL,
  `FechaHora` DATETIME NOT NULL,
  `Producto_idCodigo` CHAR(13) NOT NULL,
  `Empleado_idEmpleado` INT NOT NULL,
  PRIMARY KEY (`idEntradas_Salidas`),
  INDEX `Empleado_idEmpleado` (`Empleado_idEmpleado` ASC) VISIBLE,
  INDEX `idx_entradas_salidas_fecha` (`FechaHora` ASC) VISIBLE,
  INDEX `idx_entradas_salidas_producto` (`Producto_idCodigo` ASC) VISIBLE,
  CONSTRAINT `entradas_salidas_ibfk_1`
    FOREIGN KEY (`Producto_idCodigo`)
    REFERENCES `dbfarmacia`.`producto` (`idCodigo`),
  CONSTRAINT `entradas_salidas_ibfk_2`
    FOREIGN KEY (`Empleado_idEmpleado`)
    REFERENCES `dbfarmacia`.`empleado` (`idEmpleado`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `dbfarmacia`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dbfarmacia`.`usuario` (
  `idUsuario` INT NOT NULL,
  `NombreUsuario` VARCHAR(50) NOT NULL,
  `ContrasenaUsuario` VARCHAR(50) NOT NULL,
  `Rol` VARCHAR(20) NOT NULL,
  `Empleado_idEmpleado` INT NOT NULL,
  PRIMARY KEY (`idUsuario`),
  INDEX `Empleado_idEmpleado` (`Empleado_idEmpleado` ASC) VISIBLE,
  INDEX `idx_usuario_rol` (`Rol` ASC) VISIBLE,
  CONSTRAINT `usuario_ibfk_1`
    FOREIGN KEY (`Empleado_idEmpleado`)
    REFERENCES `dbfarmacia`.`empleado` (`idEmpleado`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
