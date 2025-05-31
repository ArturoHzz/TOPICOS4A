
-- ===========================================
-- SCRIPT COMPLETO PARA CREAR Y POBLAR LA BD
-- ===========================================

-- ========== ESTRUCTURA ==========
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


-- ========== MODIFICACIONES ==========
USE dbfarmacia;

-- 1. Eliminar claves foráneas que impiden modificar claves primarias
ALTER TABLE detalles_venta DROP FOREIGN KEY detalles_venta_ibfk_2;
ALTER TABLE detallescompra DROP FOREIGN KEY detallescompra_ibfk_1;

-- 2. Asegurar que las columnas sean claves primarias (por si acaso)
ALTER TABLE venta DROP PRIMARY KEY;
ALTER TABLE venta ADD PRIMARY KEY (idVenta);

ALTER TABLE compra DROP PRIMARY KEY;
ALTER TABLE compra ADD PRIMARY KEY (idCompra);

ALTER TABLE detalles_venta DROP PRIMARY KEY;
ALTER TABLE detalles_venta ADD PRIMARY KEY (idDetalles_Venta);

ALTER TABLE detallescompra DROP PRIMARY KEY;
ALTER TABLE detallescompra ADD PRIMARY KEY (idDetallesCompra);

-- 3. Modificar las columnas para que sean AUTO_INCREMENT
ALTER TABLE venta MODIFY COLUMN idVenta INT NOT NULL AUTO_INCREMENT;
ALTER TABLE compra MODIFY COLUMN idCompra INT NOT NULL AUTO_INCREMENT;
ALTER TABLE detalles_venta MODIFY COLUMN idDetalles_Venta INT NOT NULL AUTO_INCREMENT;
ALTER TABLE detallescompra MODIFY COLUMN idDetallesCompra INT NOT NULL AUTO_INCREMENT;

-- 4. Restaurar las claves foráneas
ALTER TABLE detalles_venta
  ADD CONSTRAINT detalles_venta_ibfk_2
  FOREIGN KEY (Venta_idVenta) REFERENCES venta(idVenta);

ALTER TABLE detallescompra
  ADD CONSTRAINT detallescompra_ibfk_1
  FOREIGN KEY (Compra_idCompra) REFERENCES compra(idCompra);


-- ========== DATOS ==========
USE dbfarmacia;

-- Categorías
INSERT INTO categoria (idCategoria, Nombre) VALUES
(1, 'Analgésicos'),
(2, 'Antibióticos'),
(3, 'Antiinflamatorios'),
(4, 'Antigripales'),
(5, 'Vitaminas'),
(6, 'Antisépticos');

-- Clientes
INSERT INTO cliente (idTelefono, Nombres, Apellidos, Correo) VALUES
('9611234567', 'Juan', 'Perez', 'juanperez@gmail.com'),
('9639876543', 'Ana', 'Garcia', 'ana.garcia@yahoo.com'),
('9611122334', 'Luis', 'Martinez', 'luis.mtz@outlook.com'),
('9634455667', 'Maria', 'Lopez', 'maria.lopez@hotmail.com'),
('9619988776', 'Jose', 'Ramirez', 'j.ramirez@gmail.com'),
('9632233445', 'Lucia', 'Fernandez', 'luciaf@gmail.com'),
('9613344556', 'Pedro', 'Castillo', 'pedro.castillo@correo.com'),
('9635566778', 'Sofia', 'Hernandez', 'sofia.hdez@mail.com'),
('1111111111', 'Cliente', 'General', 'SN');

-- Empleados
INSERT INTO empleado (idEmpleado, Nombres, Apellidos, RFC) VALUES
(1, 'Carlos', 'Ramirez', 'CARM750812Q12'),
(2, 'Sofia', 'Lopez', 'SOLP920105T89'),
(3, 'Miguel', 'Hernandez', 'MIHE850720L21'),
(4, 'Elena', 'Reyes', 'ELRE990101A10'),
(5, 'Jorge', 'Nuñez', 'JONU860512C45');

-- Proveedores
INSERT INTO proveedor (idProveedor, Nombre, Telefono, Email, Direccion, Rfc) VALUES
(1, 'Farmadistribuciones SA', '9612345678', 'contacto@farmadistribuciones.com', 'Av. Reforma 123, CDMX', 'FDS981001P12'),
(2, 'Laboratorios Saludables', '9631122334', 'ventas@saludables.mx', 'Calle Salud 456, GDL', 'LSA990202L34'),
(3, 'Distribuidora Médica Sur', '9614455667', 'ventas@medicasur.com', 'Blvd. Médico 789, TUXTLA', 'DMS951105Q32'),
(4, 'Farma Chiapas', '9635566778', 'contacto@farmachiapas.mx', 'Calle Central 102, TAPACHULA', 'FCH960615L56');

-- Formas de Pago
INSERT INTO formapago (idFormaPago, Nombre) VALUES
(1, 'Efectivo'),
(2, 'Tarjeta de Débito'),
(3, 'Tarjeta de Crédito'),
(4, 'Transferencia');

-- Unidades
INSERT INTO unidad (idUnidad, Nombre, Abreviatura) VALUES
(1, 'Miligramos', 'mg'),
(2, 'Gramos', 'g'),
(3, 'Microgramos', 'mcg'),
(4, 'Mililitros', 'mL'),
(5, 'Litros', 'L');


-- Productos
INSERT INTO producto (idCodigo, Nombre, Contenido, CostoUnitario, PrecioUnitario, Existencia, Activo, Categoria_idCategoria, Unidad_idUnidad) VALUES
('7501008494226', 'Aspirina Junior', 300, 22.00, 38.00, 50, 1, 1, 1),
('7501008498842', 'Pastillas Vitamina C', 1000, 10.00, 18.00, 120, 1, 5, 1),
('7501058715555', 'Tempra Fen', 325, 25.00, 42.00, 40, 1, 1, 1),
('7501125179983', 'Fluconazol', 150, 19.00, 33.00, 30, 1, 2, 1),
('7501125180699', 'Aciclovir', 200, 21.00, 36.00, 35, 1, 2, 1),
('7501258207409', 'Diclofenaco', 100, 18.00, 30.00, 70, 1, 3, 1),
('7501300420565', 'Aliren Antigripal Gotas', 25, 28.00, 47.00, 25, 1, 4, 4),
('7501358170863', 'Zinc', 250, 30.00, 50.00, 60, 1, 6, 4),
('7502223700093', 'Loratadina', 5, 10.00, 18.00, 20, 1, 4, 1),
('7502223709225', 'Paracetamol', 120, 14.00, 24.00, 30, 1, 1, 4),
('7502223709348', 'Omeprazol', 10, 15.00, 26.00, 18, 1, 2, 1),
('7502235760139', 'Regenesis Max', 60, 40.00, 65.00, 22, 1, 5, 1),
('7502276850530', 'Cefalexina', 500, 25.00, 40.00, 50, 1, 2, 1),
('7502276853548', 'Ibuprofeno', 400, 15.00, 25.00, 100, 1, 3, 1),
('7503006569524', 'Amoxicilina', 500, 20.00, 35.00, 80, 1, 2, 1),
('7503006098323', 'Microdacyn Solución', 250, 35.00, 58.00, 28, 1, 6, 4),
('7503036605931', 'LIFEED5', 30, 32.00, 54.00, 40, 1, 5, 1),
('7503038209887', 'Proteína Birdman Resveratrol', 500, 75.00, 120.00, 15, 1, 5, 2),
('7506472803161', 'Ácido Fólico', 5, 5.00, 9.00, 110, 1, 5, 1),
('7506472825804', 'Complejo B', 100, 20.00, 34.00, 45, 1, 5, 1);

