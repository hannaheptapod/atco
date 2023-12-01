-- CHALLENGES

WITH hackers_challenges AS (
    SELECT Hackers.hacker_id, Hackers.name, COUNT(*) AS challenge_count
    FROM Hackers
    INNER JOIN Challenges ON Hackers.hacker_id = Challenges.hacker_id
    GROUP BY Hackers.hacker_id, Hackers.name
), max_challenge_count AS (
    SELECT MAX(challenge_count) AS max_count
    FROM hackers_challenges
), less_than_max AS (
    SELECT challenge_count, COUNT(*) num
    FROM hackers_challenges
    INNER JOIN max_challenge_count ON challenge_count < max_count
    GROUP BY challenge_count
    HAVING COUNT(*) > 1
)
SELECT hc.hacker_id, hc.name, hc.challenge_count
FROM hackers_challenges hc
WHERE NOT EXISTS (
    SELECT NULL
    FROM less_than_max
    WHERE hc.challenge_count = less_than_max.challenge_count
)
ORDER BY hc.challenge_count DESC, hc.hacker_id;
