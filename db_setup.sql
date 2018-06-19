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



CREATE TABLE Proveedores (
  id INTEGER,
  nombre TEXT,
  alias TEXT,
  poblacion TEXT,
  provincia TEXT,
  cp TEXT,
  nif TEXT,
  correo TEXT,
  telefono TEXT,
  contacto TEXT,
  observaciones TEXT
);


CREATE TABLE CabeceraPedido (
  id INTEGER,
  numPedido INTEGER,
  fechaPedido DATE,
  fechaEntrega DATE,
  proveedor TEXT,
  importe TEXT,
  observaciones TEXT,
  abierto TEXT
);


CREATE TABLE CuerpoPedido (
  id INTEGER,
  numPedido INTEGER,
  codArticulo INTEGER,
  unidadPedido INTEGER,
  unidadRecibido INTEGER,
  precioCoste INTEGER,
  abierto TEXT
);



CREATE TABLE EntradaSalida (
id INTEGER,
codProveedor INTEGER,
codCliente INTEGER,
codArticulo INTEGER,
unidades INTEGER,
precio INTEGER,
fecha DATE,
tipo TEXT,
numero INTEGER);
