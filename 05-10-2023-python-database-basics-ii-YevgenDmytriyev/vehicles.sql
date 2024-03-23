CREATE DATABASE vehicles;

\c vehicles;

CREATE TABLE car_model (
    name VARCHAR(100),
    make VARCHAR(50),
    year_of_checkin VARCHAR(4),
    engine_type VARCHAR(50),
    stock INT
);
