CREATE TABLE Almacen (
  nombre TEXT,
  direccion TEXT,
  provincia TEXT,
  cp TEXT,
  telefono TEXT
);

INSERT INTO Almacen VALUES (
  "Almacenes malvavisco",
  "Calle Rua 99",
  "La Cueruña",
  "15051",
  "+34981234432"
);

INSERT INTO Almacen VALUES (
  "Almacenes Bierzo Independiente",
  "Calle Puenferrueda",
  "León",
  "24400",
  "+34987171717"
);

CREATE TABLE LineaArticulos (
  descripcion TEXT,
  pvp REAL,
  unidades INTEGER,
  ultimoCoste REAL,
  medioCoste REAL,
  stockMinimo INTEGER,
  stockSEGURIDAD INTEGER
);


/*
CREATE TABLE Proveedores (, , ,);


CREATE TABLE CabeceraPedido (, , ,);


CREATE TABLE CuerpoPedido (, , ,);


CREATE TABLE EntradaSalida (, , ,);


CREATE TABLE Mantenimiento (, , ,);


CREATE TABLE GrabacionPedidos (, , ,);


CREATE TABLE Estadisticas (, , ,);
*/
