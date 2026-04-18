DROP TABLE IF EXISTS phonebook;

CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100),
    phone VARCHAR(20) NOT NULL
);
INSERT INTO phonebook (name, surname, phone)
VALUES
('Ali', 'Serik', '87771234567'),
('Aruzhan', 'Bekova', '87011223344'),
('Shahnur','Makkambaev','87023274883'),
('Sohib','Raimov','87718857085');

-- 1

CREATE OR REPLACE FUNCTION search_phonebook(pattern_text VARCHAR)
RETURNS TABLE (
    id INT,
    name VARCHAR,
    surname VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.surname, p.phone
    FROM phonebook p
    WHERE p.name ILIKE '%' || pattern_text || '%'
       OR p.surname ILIKE '%' || pattern_text || '%'
       OR p.phone ILIKE '%' || pattern_text || '%';
END;
$$ LANGUAGE plpgsql;

-- 2 

CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_name VARCHAR,
    p_surname VARCHAR,
    p_phone VARCHAR
)
AS $$
BEGIN
    IF EXISTS(
        SELECT 1
        FROM phonebook
        WHERE name=p_name AND surname=p_surname
    ) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name AND surname = p_surname;
    ELSE
        INSERT INTO phonebook(name, surname, phone)
        VALUES(p_name, p_surname, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

-- 3

CREATE OR REPLACE PROCEDURE insert_many_users(
    names TEXT[],
    surnames TEXT[],
    phones TEXT[]
)
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^[0-9]{11}$' THEN
            INSERT INTO phonebook(name, surname, phone)
            VALUES (names[i], surnames[i], phones[i]);
        ELSE    
            RAISE NOTICE 'Incorrect phone: % for % %',
            phones[i], names[i], surnames[i];
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- 4

CREATE OR REPLACE FUNCTION get_phonebook_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(
    id INT,
    name VARCHAR,
    surname VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.surname, p.phone 
    FROM phonebook p
    ORDeR BY p.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

-- 5

CREATE OR REPLACE PROCEDURE delete_user_data(p_value VARCHAR)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_value or phone = p_value;
END;
$$ LANGUAGE plpgsql;