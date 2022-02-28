DROP TABLE IF EXISTS 'Customer';
DROP TABLE IF EXISTS 'Movie';
DROP TABLE IF EXISTS 'Store';
DROP TABLE IF EXISTS 'Catelog';
DROP TABLE IF EXISTS 'Active_Rentals';
DROP TABLE IF EXISTS 'Transactions';

-- ----------------------------------------
 CREATE TABLE IF NOT EXISTS 'Customer'(
     --Attributes
     'customer_id' int(11) NOT NULL,
     'customer_name' varchar(10) NOT NULL, 
     'customer_email' varchar(20) NOT NULL,
     PRIMARY KEY ('customer_id')
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
