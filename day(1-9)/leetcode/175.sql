-- 175. Combine Two Tables
-- Write your PostgreSQL query statement below
select firstName, lastName, city, state from person left join address on address.personid = person.personid;