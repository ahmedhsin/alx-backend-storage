-- first procedure
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	DECLARE avgScore FLOAT;
	SET avgScore = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
	UPDATE users SET average_score = avgScore WHERE id = user_id;
END;$$
DELIMITER ;
