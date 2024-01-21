-- first procedure
  
DELIMITER $$
CREATE FUNCTION GetWeightScore(score INT, project_id INT)
RETURNS float
BEGIN
DECLARE answer float;
SET answer = (SELECT weight FROM projects WHERE id = project_id) * score;
RETURN(answer);

END;$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
        DECLARE avgScore FLOAT;
        SET avgScore = (SELECT AVG(getWeightScore(score, project_id)) FROM corrections WHERE corrections.user_id = user_id);
        UPDATE users SET average_score = avgScore WHERE id = user_id;
END;$$
DELIMITER ;

