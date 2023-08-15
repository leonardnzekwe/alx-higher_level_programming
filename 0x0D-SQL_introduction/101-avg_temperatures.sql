-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- Retrieves the average temperature of distinct cities and sort them in descending order
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM temperatures
GROUP BY `city`
ORDER BY `avg_temp` DESC;
