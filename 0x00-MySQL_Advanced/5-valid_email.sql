-- Initial
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id int not null AUTO_INCREMENT,
    email varchar(255) not null,
    name varchar(255),
    valid_email boolean not null default 0,
    PRIMARY KEY (id)
);

INSERT INTO users (email, name) VALUES ("bob@dylan.com", "Bob");
INSERT INTO users (email, name, valid_email) VALUES ("sylvie@dylan.com", "Sylvie", 1);
INSERT INTO users (email, name, valid_email) VALUES ("jeanne@dylan.com", "Jeanne", 1);

--A trigger that resets the attribute valid_email
-- only when the email has been changed.
DELIMITER $$;

CREATE TRIGER update_email_validator
AFTER UPDATE
ON users
FOR EACH ROW
BEGIN
UPDATE users
SET valid_email=1
WHERE email=New.email;
END$$

DELIMITER ;$$
