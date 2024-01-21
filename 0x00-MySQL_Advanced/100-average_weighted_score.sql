-- first procedure
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DROP FUNCTION IF EXISTS GetWeight;
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
DELIMITER ;

