# Write your MySQL query statement below
SELECT e.name as Employee
from Employee e
join Employee m on e.managerId = m.id
where e.salary > m.salary