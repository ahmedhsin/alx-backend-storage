-- f function 
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS float
BEGIN
DECLARE answer float;
IF b = 0 THEN
 SET answer = 0;
ELSE
 SET answer = a/b;
END IF;
RETURN(answer);

END;$$
DELIMITER ;
