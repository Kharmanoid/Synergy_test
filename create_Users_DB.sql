DROP DATABASE IF EXISTS Users;
CREATE DATABASE Users;
USE Users;

CREATE TABLE courses (id   INT AUTO_INCREMENT PRIMARY KEY,
                      code VARCHAR(8) NOT NULL UNIQUE,
                      name VARCHAR(20) NOT NULL
);

CREATE TABLE listeners (id     INT AUTO_INCREMENT PRIMARY KEY,
                        name   VARCHAR(50) NOT NULL,
                        mail   VARCHAR(40) NOT NULL UNIQUE,
                        phone  VARCHAR(15) UNIQUE,
                        mobile VARCHAR(15) UNIQUE,
                        status ENUM('Inactive', 'Active') DEFAULT 'Inactive'
);

CREATE TABLE finishedCourses (course_id   INT,
                              listener_id INT,
                              FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
                              FOREIGN KEY (listener_id) REFERENCES listeners(id) ON DELETE CASCADE,
                              PRIMARY KEY (course_id, listener_id)
);

INSERT INTO courses (code, name) VALUES ('A0123656', 'Python-Base');
INSERT INTO courses (code, name) VALUES ('A0184656', 'Python-Database');
INSERT INTO courses (code, name) VALUES ('B0167256', 'HTML');
INSERT INTO courses (code, name) VALUES ('C3842656', 'Java-Base');
INSERT INTO courses (code, name) VALUES ('D6183456', 'JavaScript-Base');

INSERT INTO listeners (name, mail) VALUES ('Sebastian Vettel', 'vet@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Lewis Hamilton', 'ham@gmail.com');                              
INSERT INTO listeners (name, mail) VALUES ('Valtteri Bottas', 'bot@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Kimi Raikkonen', 'rai@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Daniel Ricciardo', 'ric@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Max Verstappen', 'ver@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Sergio Perez', 'per@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Carlos Sainz', 'sai@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Felipe Massa', 'mas@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Esteban Ocon', 'oco@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Nico Hulkenberg', 'hul@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Romain Grosjean', 'gro@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Kevin Magnussen', 'mag@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Pascal Wehrlein', 'weh@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Daniil Kvyat', 'kvy@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Jolyon Palmer', 'pal@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Marcus Ericsson', 'eri@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Lance Stroll', 'str@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Fernando Alonso', 'alo@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Antonio Giovinazzi', 'gio@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Stoffel Vandoorne', 'van@gmail.com');
INSERT INTO listeners (name, mail) VALUES ('Jenson Button', 'but@gmail.com');

DELIMITER //
CREATE PROCEDURE getListeners ()
BEGIN
	SELECT id, name, mail, status 
    FROM listeners;
END//

CREATE PROCEDURE getListenerDetail (IN user_id INT)
BEGIN
	SELECT listeners.*,
	GROUP_CONCAT( CONCAT(courses.id, ',', courses.name) SEPARATOR ';') AS courses 
	FROM listeners
	LEFT JOIN finishedCourses ON listeners.id = finishedCourses.listener_id
	LEFT JOIN courses ON courses.id = finishedCourses.course_id
    WHERE listeners.id = user_id
	GROUP BY listeners.name;
END//

CREATE PROCEDURE addListener (IN user_name VARCHAR(50),
                              IN user_mail VARCHAR(40),
                              IN user_phone  VARCHAR(15),
                              IN user_mobile  VARCHAR(15),
                              IN user_status INT)
BEGIN
	INSERT INTO listeners (name, mail, phone, mobile, status) 
    VALUES (user_name, user_mail, user_phone, user_mobile, user_status);
END//

CREATE PROCEDURE editListener (IN user_id INT,
                               IN user_mail VARCHAR(40),
                               IN user_phone  VARCHAR(15),
                               IN user_mobile  VARCHAR(15),
                               IN user_status INT)
BEGIN
	UPDATE LOW_PRIORITY listeners 
    SET mail = user_mail, phone = user_phone, mobile = user_mobile, status = user_status
    WHERE id = user_id;
END//

CREATE PROCEDURE removeListener (IN user_id INT)
BEGIN
	DELETE FROM listeners 
    WHERE id = user_id;
END//

CREATE PROCEDURE addListenerCourse (IN listener INT,
									IN course INT)
BEGIN
	INSERT IGNORE INTO finishedCourses (listener_id, course_id) 
    VALUES (listener, course);
END//

CREATE PROCEDURE getCourses ()
BEGIN
	SELECT * FROM courses;
END//

CREATE PROCEDURE getCourseName (IN course_id INT)
BEGIN
	SELECT name FROM courses
    WHERE courses.id = course_id;
END//
DELIMITER ;
