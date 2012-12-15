SELECT * FROM Encuesta WHERE Id = 19;

SELECT * FROM Encuesta;

SELECT Id, Fecha, DATE_FORMAT(Fecha, '%d/%m/%Y'), IdEncuestador, Observacion FROM Encuesta;

-- 2012-09-30
-- 2012-09-30T17:12:07
-- DATE_FORMAT(date,format)
SELECT DATE_FORMAT(CURRENT_TIMESTAMP(), '%d/%m/%Y');

SELECT STR_TO_DATE('01,5,2013','%d,%m,%Y');

SELECT * FROM Encuestador;


SHOW TABLES;

SELECT * FROM Familia;



DELETE FROM Encuesta;



ALTER TABLE Familia
    ADD COLUMN `Lote` VARCHAR(10) NULL;
	 
	 
	 
	 
	 
ALTER TABLE Familia
    DROP COLUMN `FechaEncuesta`;
	 
	 
SELECT * FROM Colonia;


SELECT
  fa."Id" AS "Id", co."Nombre" AS "Colonia", ca."Nombre" AS "Calle", fa."Lote" AS "Lote", fa."NoExt" AS "NoExt", fa."NoInt" AS "NoInt" 
FROM
  "Familia" AS fa INNER JOIN
  "Calle" AS ca ON ca."Id" = fa."IdCalle" INNER JOIN
  "Manzana" AS ma ON ma."Id" = fa."IdManzana" INNER JOIN
  "Colonia" AS co ON co."Id" = ca."IdColonia"
  

  
  
SELECT
  p."Id" AS "Id", p."Nombre" AS "Nombre", pa."Nombre" AS "Parentesco", p."Edad" AS "Edad", re."Nombre" AS "Religion"
FROM
  "Persona" p INNER JOIN
  "Parentesco" pa ON p."IdParentesco" = pa."Id" INNER JOIN
  "Religion" re ON p."IdReligion" = re."Id"
--WHERE
--  p."IdFamilia" = 1


