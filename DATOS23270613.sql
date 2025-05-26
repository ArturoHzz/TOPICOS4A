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
('9635566778', 'Sofia', 'Hernandez', 'sofia.hdez@mail.com');

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
INSERT INTO producto (
  idCodigo, Nombre, Contenido, CostoUnitario, PrecioUnitario,
  Existencia, Activo, Categoria_idCategoria, Unidad_idUnidad
) VALUES
('7502223709225', 'Paracetamol', 500, 20.00, 31.00, 50, 1, 1, 1),
('7502223709348', 'Omeprazol', 20, 80.00, 133.00, 20, 1, 2, 1),
('7502276853548', 'Ibuprofeno', 400, 15.00, 25.00, 100, 1, 3, 1),
('7503006569524', 'Amoxicilina', 500, 20.00, 35.00, 80, 1, 2, 1),
('7501008498842', 'Pastillas Vitamina C', 1000, 10.00, 18.00, 120, 1, 5, 1),
('7502223700093', 'Loratadina', 10, 12.00, 20.00, 90, 1, 4, 1),
('7501358170863', 'Zinc', 250, 30.00, 50.00, 60, 1, 6, 4),
('7501258207409', 'Diclofenaco', 100, 18.00, 30.00, 70, 1, 3, 1),
('7502276850530', 'Cefalexina', 500, 25.00, 40.00, 50, 1, 2, 1),
('7506472803161', 'Ácido Fólico', 5, 5.00, 9.00, 110, 1, 5, 1);
