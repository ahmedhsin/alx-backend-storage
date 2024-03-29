-- trigger for store
DELIMITER $$
CREATE TRIGGER decrease_after_add
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END;$$
DELIMITER ;
