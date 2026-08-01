

#1 Display all airlines with their IATA codes
SELECT airline_name, iata_code
FROM airlines;


#2 Find the total number of airports
SELECT COUNT(*) AS Total_Airports
FROM airports;




#3 List the top 10 busiest airports
SELECT airport_name, total_passengers_boarding_2023
FROM airports
ORDER BY total_passengers_boarding_2023 DESC
LIMIT 10;




#4 Find all Delayed Flights
SELECT * FROM flights
WHERE flight_status='Delayed';




#5 Count flights by status
SELECT flight_status, COUNT(*) AS Total_Flights
FROM flights
GROUP BY flight_status;




#6 Average delay minutes
SELECT AVG(delay_minutes)
FROM flights
WHERE delay_minutes>10;



#7 Find cancelled flights
SELECT * FROM flights
WHERE flight_status='Cancelled';




#8 Top airlines having maximum flights
SELECT airline_id, COUNT(*) AS Total_flights
FROM flights
GROUP BY airline_id
ORDER BY total_flights DESC;



#9 Weather conditions frequency
SELECT conditions, COUNT(*) 
FROM weather 
GROUP BY conditions;



#10 Longest flight route
SELECT * FROM routes
ORDER BY distance_miles DESC
LIMIT 10;














