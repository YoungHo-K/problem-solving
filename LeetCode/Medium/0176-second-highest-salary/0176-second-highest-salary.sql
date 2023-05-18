# Write your MySQL query statement below
with distinct_salary as (
    select distinct salary
    from Employee
    ), 
    ordered_salary as (
        select row_number() over (order by salary desc) as no, salary
        from distinct_salary
    ) 
    select max(salary) as SecondHighestSalary from ordered_salary where no = 2;
