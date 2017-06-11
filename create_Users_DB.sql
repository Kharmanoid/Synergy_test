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
                        status ENUM('Active', 'Inactive') DEFAULT 'Inactive'
);

CREATE TABLE finishedCourses (course_id   INT,
                              listener_id INT,
                              FOREIGN KEY (course_id) REFERENCES courses(id),
                              FOREIGN KEY (listener_id) REFERENCES listeners(id)
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