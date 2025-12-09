# Write your MySQL query statement below

Select P.firstName , P.lastName , A.city , A.state
From Person as P
left Join Address as A on A.personId = P.personId