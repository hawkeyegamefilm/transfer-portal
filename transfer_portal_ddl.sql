--basic transfer_portal
create table transfer_portal (
id serial,
season char(4),
first_name varchar(50),
last_name varchar(50),
position varchar(5),
origin varchar(50),
destination varchar(50),
transfer_date date,
rating decimal,
stars smallint,
eligibility varchar(50)
)

--sub in the appropriate file location
COPY transfer_portal(season,first_name,last_name,position,origin,destination,transfer_date,rating,stars,eligibility)
FROM 'C:\data\transfer_portal_2023_2_22_2023.csv'
DELIMITER ','
CSV HEADER;
