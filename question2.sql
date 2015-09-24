create table salesperson
  (ID number(3),
    Name varchar(15),
    Age number(3),
    Salary number(6));

INSERT INTO salesperson (ID)
VALUES ('1','2','5','7','8','11')

INSERT INTO salesperson (Name)
VALUES ('Abe','Bob','Chris','Dan','Ken','Joe')

INSERT INTO salesperson (Age)
VALUES ('61','34','34','41','57','38')

INSERT INTO salesperson (Salary)
VALUES ('140000','44000','40000','52000','115000','38000')


create table orders
  (OrderNumber number(3),
    OrderDate date(8),
    CustID number(3),
    SalespersonID number(3),
    Amount number(5));


SELECT name
FROM orders, salesperson
WHERE orders.salesperson_id = salsesperson.salesperson_id
GROUP By name, salesperson_id
HAVING COUNT (Salesperson_id) > 1
