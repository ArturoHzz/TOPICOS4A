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
INSERT INTO producto (idCodigo, Nombre, Contenido, CostoUnitario, PrecioUnitario, Existencia, Activo, Categoria_idCategoria, Unidad_idUnidad) VALUES
('7501008494226', 'Aspirina Junior', 300, 22.00, 38.00, 50, 1, 1, 1),
('7501008498842', 'Pastillas Vitamina C', 1000, 10.00, 18.00, 120, 1, 5, 1),
('7501058715555', 'Tempra Fen', 325, 25.00, 42.00, 40, 1, 1, 1),
('7501125179983', 'Fluconazol', 150, 19.00, 33.00, 30, 1, 2, 1),
('7501125180699', 'Aciclovir', 200, 21.00, 36.00, 35, 1, 2, 1),
('7501258207409', 'Diclofenaco', 100, 18.00, 30.00, 70, 1, 3, 1),
('7501300420565', 'Aliren Antigripal Gotas', 25, 28.00, 47.00, 25, 1, 4, 4),
('7501358170863', 'Zinc', 250, 30.00, 50.00, 60, 1, 6, 4),
('750223700093',  'Loratadina Infantil', 5, 10.00, 18.00, 20, 1, 4, 1),
('750223709225',  'Paracetamol Jarabe', 120, 14.00, 24.00, 30, 1, 1, 4),
('750223709348',  'Omeprazol Infantil', 10, 15.00, 26.00, 18, 1, 2, 1),
('7502235760139', 'Regenesis Max', 60, 40.00, 65.00, 22, 1, 5, 1),
('7502276850530', 'Cefalexina', 500, 25.00, 40.00, 50, 1, 2, 1),
('7502276853548', 'Ibuprofeno', 400, 15.00, 25.00, 100, 1, 3, 1),
('7503006569524', 'Amoxicilina', 500, 20.00, 35.00, 80, 1, 2, 1),
('7503006098323', 'Microdacyn Solución', 250, 35.00, 58.00, 28, 1, 6, 4),
('7503036605931', 'LIFEED5', 30, 32.00, 54.00, 40, 1, 5, 1),
('7503038209887', 'Proteína Birdman Resveratrol', 500, 75.00, 120.00, 15, 1, 5, 2),
('7506472803161', 'Ácido Fólico', 5, 5.00, 9.00, 110, 1, 5, 1),
('7506472825804', 'Complejo B', 100, 20.00, 34.00, 45, 1, 5, 1);
