USE COMP3278_G12;

INSERT INTO  Customer (customer_id,lastname,firstname,gender,birthday,email,phone,certification_type,id_number,password) VALUES
 ('001','Ma','Jack','male','2020-11-01','@gmail.com','12345678','student card',0000011111,'iamjack'),
 ('002','Richeal','Rose','female','2020-11-17','@gmail.com','12345678','student card',1111100000,'iamjacks'),
 ('003','Yan','Zipeng','male','2000-10-17','@gmail.com','12345678','student card',0000011111,'password1'),
 ('004','Zhu','Jiarui','female','2020-11-01','@gmail.com','12345678','student card',0000011111,'password2'),
 ('005','Huang','Haoyu','male','2020-11-01','@gmail.com','12345678','student card',0000011111,'password3'),
 ('006','Ye','Mao','male','2020-11-01','@gmail.com','12345678','student card',0000011111,'password4'),
 ('007','Bai','Qingyu','female','2020-11-01','@gmail.com','12345678','student card',0000011111,'password5');

 INSERT INTO CustomerHistory (from_customer_id, login_date, login_time) VALUES
 ('001','2021-10-30', '23:59:59'),
 ('002','2021-10-31', '12:40:59'),
 ('003','2021-10-29', '23:59:59'),
 ('004','2021-10-15', '00:59:30'),
 ('005','2021-10-11', '23:40:59'),
 ('006','2021-11-01', '13:59:59'),
 ('007','2021-11-05', '23:59:30');

 INSERT INTO Frequent_contact (from_customer_id, to_customer_id, last_transfer_date) VALUES
 ('001','002','2021-10-30'),
 ('002','001','2021-10-30'),
 ('003','002','2021-09-30'),
 ('004','002','2021-09-30'),
 ('005','003','2021-09-30'),
 ('006','002','2021-09-30'),
 ('007','002','2021-09-30');

 INSERT INTO Account (account_id, customer_id, create_time, currency_type) VALUES
 ('001','001','1900-10-10','Pound'),
 ('002','001','1910-10-10','Pound'),
 ('003','002','1910-10-10','Pound'),
 ('004','002','1911-10-10','Pound'),
 ('005','002','1912-10-10','Pound'),
 ('006','004','2000-10-10','Hong Kong Dollar'),
 ('007','005','2000-10-10','Hong Kong Dollar'),
 ('008','006','2000-10-10','Hong Kong Dollar'),
 ('009','007','2000-10-10','Hong Kong Dollar'),
 ('010','001','1915-10-10','Pound'),
 ('011','002','1920-11-11','Pound');

 INSERT INTO Investment_account (account_id, customer_id, currency_type, create_time, total_value) VALUES
 ('002','001','Pound','1910-10-10',1000000),
 ('003','002','Pound','1910-10-10',202020),
 ('008','006','Hong Kong Dollar','2000-10-10',1000000);

 INSERT INTO Saving_account (account_id, customer_id, currency_type, create_time, balance) VALUES
 ('001','001','Pound','1900-10-10',15000),
 ('004','002','Pound','1911-10-10',14000),
 ('006','004','Hong Kong Dollar','2000-10-10',10000),
 ('007','005','Hong Kong Dollar','2000-10-10',20000),
 ('008','006','Hong Kong Dollar','2000-10-10',12000),
 ('009','007','Hong Kong Dollar','2000-10-10',1000);

 INSERT INTO Credit_account (account_id, customer_id, currency_type, create_time, total_debt) VALUES
 ('010','001','Pound','1915-10-10',10000),
 ('011','002','Pound','1920-11-11',10000);

INSERT INTO Transaction (transaction_id, in_account_id, out_account_id, in_customer_id, out_customer_id, amount, timepoint_date, timepoint_time) VALUES
('001','001','004','001','002',520,'1952-05-20','00:00:01'),
('002','001','004','001','002',1000,'1960-05-20','00:10:01'),
('003','001','004','001','002',520,'1970-05-20','10:10:01'),
('004','004','001','002','001',520,'1952-05-20','00:30:01'),
('005','004','001','002','001',520,'1960-05-20','00:30:01'),
('006','004','001','002','001',520,'1970-05-20','01:30:01');

INSERT INTO Product (product_id, type, price, holdings, issuer) VALUES
('001','A1',100,'NULL','NULL'),
('002','B2',200,'NULL','NULL'),
('003','C3',10,'NULL','NULL'),
('004','D4',10,'NULL','NULL');

INSERT INTO Loan (loan_id, interest_rate) VALUES
('001',5000),
('002',4955);

INSERT INTO Product_contain (product_id, account_id, holdings, product_values) VALUES
('001','002','NULL',100000),
('002','002','NULL',100000),
('004','002','NULL',100000),
('003','003','NULL',100000);

INSERT INTO Loan_contain (loan_id, account_id, borrow_time, next_due_time, unpaid_amount) VALUES
('001','010','2020-09-01','2022-09-01',1000000),
('002','011','2020-09-01','2022-09-01',1000000);
