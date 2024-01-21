-- first procedure
  
DELIMITER $$
CREATE FUNCTION GetWeight(project_id INT)
RETURNS float
BEGIN
DECLARE answer float;
SET answer = (SELECT weight FROM projects WHERE id = project_id);
RETURN(answer);

END;$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
        DECLARE avgScore FLOAT;
        DECLARE	totalWeight FLOAT;
        SET totalWeight = (SELECT SUM(GetWeight(project_id)) FROM corrections WHERE corrections.user_id = user_id);
        SET avgScore = (SELECT SUM(GetWeight(project_id)*score) FROM corrections WHERE corrections.user_id = user_id);
        UPDATE users SET average_score = avgScore/totalWeight WHERE id = user_id;
END;$$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser ()
BEGIN
	DECLARE user_id INT;
	DECLARE userCursor CURSOR FOR SELECT id FROM users;
	OPEN userCursor;
	userLoop: LOOP
	FETCH userCursor INTO user_id;
	IF done THEN
	LEAVE userLoop;
	END IF;
	CALL ComputeAverageWeightedScoreForUser(user_id);
	END LOOP;
END$$

DELIMITER ;

