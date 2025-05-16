USE dbfarmacia;

-- Clientes
INSERT INTO cliente (idTelefono, Nombres, Apellidos, Correo) VALUES
('9611234567', 'Juan', 'Pérez', 'juanperez@gmail.com'),
('9639876543', 'Ana', 'García', 'ana.garcia@yahoo.com'),
('9611122334', 'Luis', 'Martínez', 'luis.mtz@outlook.com'),
('9634455667', 'María', 'López', 'maria.lopez@hotmail.com'),
('9619988776', 'José', 'Ramírez', 'j.ramirez@gmail.com'),
('9632233445', 'Lucía', 'Fernández', 'luciaf@gmail.com'),
('9613344556', 'Pedro', 'Castillo', 'pedro.castillo@correo.com'),
('9635566778', 'Sofía', 'Hernández', 'sofia.hdez@mail.com');

-- Empleados
INSERT INTO empleado (idEmpleado, Nombres, Apellidos, RFC) VALUES
(1, 'Carlos', 'Ramírez', 'CARM750812Q12'),
(2, 'Sofía', 'López', 'SOLP920105T89'),
(3, 'Miguel', 'Hernández', 'MIHE850720L21'),
(4, 'Elena', 'Reyes', 'ELRE990101A10'),
(5, 'Jorge', 'Núñez', 'JONU860512C45');

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
(4, 'Transferencia'),
(5, 'Vales');

-- Unidades
INSERT INTO unidad (idUnidad, Nombre, Abreviatura) VALUES
(1, 'Miligramos', 'mg'),
(2, 'Gramos', 'g'),
(3, 'Microgramos', 'mcg'),
(4, 'Mililitros', 'mL'),
(5, 'Litros', 'L');
