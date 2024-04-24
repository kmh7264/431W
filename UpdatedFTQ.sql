-- Database: FlightData

-- DROP DATABASE IF EXISTS "FlightData";

CREATE DATABASE "FlightData"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
	


Create table Airline as 
select distinct on ("Flight_Number_Marketing_Airline")
	"Flight_Number_Marketing_Airline",
	"Airline", 
	"Marketing_Airline_Network",  
	"IATA_Code_Marketing_Airline", 
	"DOT_ID_Marketing_Airline",
	"Operated_or_Branded_Code_Share_Partners" 
from "FSP";

alter table Airline 
add primary key("Flight_Number_Marketing_Airline");

Create table Origin as 
select distinct on ("OriginAirportID")
	"OriginAirportID",
    "OriginAirportSeqID",
    "OriginCityMarketID",
    "OriginCityName",
    "OriginState",
    "OriginStateFips",
    "OriginStateName",
    "OriginWac"
from "FSP";

alter table Origin 
add primary key("OriginAirportID");


Create table Destination as 
select distinct on ("DestAirportID")
	"DestAirportID",
    "DestAirportSeqID",
    "DestCityMarketID",
    "DestCityName",
    "DestState",
    "DestStateFips",
    "DestStateName",
    "DestWac",
	"DivAirportLandings"
from "FSP";

alter table Destination 
add primary key("DestAirportID");

create table Period as 
select distinct on ("FlightDate")
	"FlightDate",
	"Year",
    "Quarter",
    "Month",
    "DayofMonth",
    "DayOfWeek"
from "FSP";

alter table Period 
add primary key ("FlightDate");


Create table Length as 
select distinct on ("Tail_Number")
	"Tail_Number",
	"AirTime", 
	"DistanceGroup",
	"ActualElapsedTime", 
	"Distance"
from "FSP";

alter table Length 
add primary key("Tail_Number");

create table Flight_Schedule as 
select distinct on ("Tail_Number")
	"Tail_Number",
	"OriginAirportID",
	"DestAirportID",
	"FlightDate", 
	"CRSArrTime", 
	"ArrTime", 
	"CRSDepTime", 
	"DepTime",
	"CRSElapsedTime",
	"Distance"
from "FSP";
 

alter table Flight_Schedule 
add primary key("Tail_Number");


create table Status as 
select distinct on ("Tail_Number")
	"Tail_Number",
	"DepDelay",
	"DepDel15",
    "DepartureDelayGroups",
	"DepDelayMinutes",
	"ArrDelay",
    "ArrDel15",
    "ArrivalDelayGroups",
	"ArrDelayMinutes",
	"Cancelled",
    "Diverted", 
	"DivAirportLandings"
from "FSP";

alter table Status 
add primary key("Tail_Number");

select * from "FSP";
drop table Logistics;

create table Logistics as 
select distinct on ("Tail_Number")
	"Tail_Number",
    "Flight_Number_Operating_Airline",
	"ArrTimeBlk",
	"DepTimeBlk",
    "TaxiOut",
    "WheelsOff",
    "WheelsOn",
    "TaxiIn",
    "Operating_Airline",
    "DOT_ID_Operating_Airline",
    "IATA_Code_Operating_Airline"
from "FSP";

alter table Logistics
add primary key("Tail_Number");
select * from Logistics;


Insert into Origin("OriginAirportID", "OriginAirportSeqID", "OriginCityMarketID","OriginCityName", "OriginState", "OriginStateFips","OriginStateName") values (19999,1999999,39999,'Pitt','PA',42,'Pennsylvania');

Delete from Origin where "OriginAirportID" = 19999;

update Origin set "OriginCityName" = 'Pittsburgh' where "OriginCityName" = 'Pitt';

select * from Origin where "OriginState" = 'PA'; 

Select COUNT("Tail_Number") from Flight; 

select * from length order by "AirTime" desc, "Distance" desc;

select * from Flight_Schedule F join Status S on F."Tail_Number" = S."Tail_Number";

select "Quarter", COUNT(*) as period_count from Period group by "Quarter";

select * from Flight_Schedule where "Tail_Number" in (Select "Tail_Number" from Status where "DepDelay" > 0);
