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
