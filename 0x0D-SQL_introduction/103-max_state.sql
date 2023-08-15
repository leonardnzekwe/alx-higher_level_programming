-- a script that displays the max temperature of each state (ordered by State name)
-- Retrieves `state` that has the max temp `value` from the `temperatures` table in the current database
SELECT `state`, MAX(`value`) AS `max_temp`
FROM temperatures
GROUP BY `state`
ORDER BY `state`;
