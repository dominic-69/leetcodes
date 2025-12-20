# Write your MySQL query statement below
select name AS customers 
from customers 
WHERE id NOT IN(
    select customerId from orders
);