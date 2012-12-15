
--
-- Current Database: "censocath"
--

--
-- Pragmas
--
PRAGMA encoding = "UTF-8";

DROP TABLE IF EXISTS "Colonia";

DROP TABLE IF EXISTS "Calle";

DROP TABLE IF EXISTS "Encuesta";

DROP TABLE IF EXISTS "Encuestador";

DROP TABLE IF EXISTS "Familia";

DROP TABLE IF EXISTS "Manzana";

DROP TABLE IF EXISTS "Parentesco";

DROP TABLE IF EXISTS "Persona";

DROP TABLE IF EXISTS "Religion";

DROP TABLE IF EXISTS "Sexo";

-- =========================================================================

--
-- Table structure for table "Religion"
--

CREATE TABLE "Religion" (
  "Id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Nombre" TEXT DEFAULT NULL
);


--
-- Dumping data for table "Religion"
--

INSERT INTO "Religion" ("Id", "Nombre") VALUES (1,'CatÃ³lica');
INSERT INTO "Religion" ("Id", "Nombre") VALUES (2,'Cristiana');
INSERT INTO "Religion" ("Id", "Nombre") VALUES (3,'Santos de los Ãšltimos dÃ­as');
INSERT INTO "Religion" ("Id", "Nombre") VALUES (4,'Testigos de JehovÃ¡');
INSERT INTO "Religion" ("Id", "Nombre") VALUES (5,'Piedra Angular');
INSERT INTO "Religion" ("Id", "Nombre") VALUES (6,'Luz del dÃ­a');
INSERT INTO "Religion" ("Id", "Nombre") VALUES (7,'Mormones');
INSERT INTO "Religion" ("Id", "Nombre") VALUES (8,'JudÃ­os');
INSERT INTO "Religion" ("Id", "Nombre") VALUES (9,'Budistas');
INSERT INTO "Religion" ("Id", "Nombre") VALUES (10,'Otros');



--
-- Table structure for table "Sexo"
--

CREATE TABLE "Sexo" (
  "Id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Nombre" TEXT DEFAULT NULL
);

--
-- Dumping data for table "Sexo"
--

INSERT INTO "Sexo" ("Id", "Nombre") VALUES (1,'Hombre');
INSERT INTO "Sexo" ("Id", "Nombre") VALUES (2,'Mujer');
INSERT INTO "Sexo" ("Id", "Nombre") VALUES (3,'Otro');



--
-- Table structure for table "Encuestador"
--


CREATE TABLE "Encuestador" (
  "Id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Nombre" TEXT DEFAULT NULL
);


--
-- Dumping data for table "Encuestador"
--



INSERT INTO "Encuestador" ("Id", "Nombre") VALUES (1,'Otro');
INSERT INTO "Encuestador" ("Id", "Nombre") VALUES (2,'Esperanza MÃ¡rquez MÃ©ndez');



--
-- Table structure for table "Parentesco"
--


CREATE TABLE "Parentesco" (
  "Id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Nombre" TEXT DEFAULT NULL
);


--
-- Dumping data for table "Parentesco"
--

INSERT INTO "Parentesco" ("Id", "Nombre") VALUES (1,'Padre');
INSERT INTO "Parentesco" ("Id", "Nombre") VALUES (2,'Madre');
INSERT INTO "Parentesco" ("Id", "Nombre") VALUES (3,'Hijo');
INSERT INTO "Parentesco" ("Id", "Nombre") VALUES (4,'Hija');
INSERT INTO "Parentesco" ("Id", "Nombre") VALUES (5,'Otro');



--
-- Table structure for table "Colonia"
--

CREATE TABLE "Colonia" (
  "Id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Nombre" TEXT DEFAULT NULL
);


--
-- Dumping data for table "Colonia"
--

INSERT INTO "Colonia" ("Id", "Nombre") VALUES (1,'San Pablo Xochimehuacan');
INSERT INTO "Colonia" ("Id", "Nombre") VALUES (2,'Santa BÃƒÂ¡rbara');
INSERT INTO "Colonia" ("Id", "Nombre") VALUES (3,'Mariscal');
INSERT INTO "Colonia" ("Id", "Nombre") VALUES (4,'Barranca Honda');
INSERT INTO "Colonia" ("Id", "Nombre") VALUES (5,'28 de Octubre');
INSERT INTO "Colonia" ("Id", "Nombre") VALUES (6,'Francisco I. Madero');
INSERT INTO "Colonia" ("Id", "Nombre") VALUES (7,'Miravalle');


--
-- Table structure for table "Calle"
--


CREATE TABLE "Calle" (
  "Id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Nombre" TEXT DEFAULT NULL,
  "IdColonia" INTEGER DEFAULT NULL,
  "IdSector" INTEGER DEFAULT NULL,
  CONSTRAINT "Calle_FK01" FOREIGN KEY ("IdColonia") REFERENCES "Colonia" ("Id")
);


--
-- Dumping data for table "Calle"
--




--
-- Table structure for table "Manzana"
--


CREATE TABLE "Manzana" (
  "Id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Nombre" TEXT DEFAULT NULL,
  "IdColonia" INTEGER DEFAULT NULL,
  "IdSector" INTEGER DEFAULT NULL,
  "IdCalle" INTEGER DEFAULT NULL,
  CONSTRAINT "Manzana_FK01" FOREIGN KEY ("IdCalle") REFERENCES "Calle" ("Id"),
  CONSTRAINT "Manzana_FK02" FOREIGN KEY ("IdColonia") REFERENCES "Colonia" ("Id")
);


--
-- Dumping data for table "Manzana"
--







--
-- Table structure for table "Encuesta"
--



CREATE TABLE "Encuesta" (
  "Id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Fecha" datetime DEFAULT NULL,
  "IdEncuestador" INTEGER DEFAULT NULL,
  "Observacion" TEXT DEFAULT NULL,
  CONSTRAINT "Encuesta_FK01" FOREIGN KEY ("IdEncuestador") REFERENCES "Encuestador" ("Id")
);


--
-- Dumping data for table "Encuesta"
--



--
-- Table structure for table "Familia"
--



CREATE TABLE "Familia" (
  "Id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "IdCalle" INTEGER DEFAULT NULL,
  "IdManzana" INTEGER DEFAULT NULL,
  "IdEncuesta" INTEGER DEFAULT NULL,
  "NoExt" TEXT DEFAULT NULL,
  "NoInt" TEXT DEFAULT NULL,
  "Lote" TEXT DEFAULT NULL,
  CONSTRAINT "Familia_FK01" FOREIGN KEY ("IdCalle") REFERENCES "Calle" ("Id"),
  CONSTRAINT "Familia_FK02" FOREIGN KEY ("IdManzana") REFERENCES "Manzana" ("Id"),
  CONSTRAINT "Familia_FK03" FOREIGN KEY ("IdEncuesta") REFERENCES "Encuesta" ("Id")
);


--
-- Dumping data for table "Familia"
--



--
-- Table structure for table "Persona"
--


CREATE TABLE "Persona" (
  "Id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "IdParentesco" INTEGER DEFAULT NULL,
  "Nombre" TEXT DEFAULT NULL,
  "Edad" INTEGER DEFAULT NULL,
  "IdSexo" INTEGER DEFAULT NULL,
  "IdReligion" INTEGER DEFAULT NULL,
  "LugarOrigen" TEXT DEFAULT NULL,
  "IdFamilia" INTEGER DEFAULT NULL,
  CONSTRAINT "Persona_FK01" FOREIGN KEY ("IdFamilia") REFERENCES "Familia" ("Id"),
  CONSTRAINT "Persona_FK02" FOREIGN KEY ("IdParentesco") REFERENCES "Parentesco" ("Id"),
  CONSTRAINT "Persona_FK03" FOREIGN KEY ("IdReligion") REFERENCES "Religion" ("Id"),
  CONSTRAINT "Persona_FK04" FOREIGN KEY ("IdSexo") REFERENCES "Sexo" ("Id")
);


--
-- Dumping data for table "Persona"
--



-- Migration completed on 2012-12-01  2:53:32
