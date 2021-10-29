DROP DATABASE IF EXISTS `COMP3278_G12`;
CREATE DATABASE `COMP3278_G12`;
USE `COMP3278_G12`;

CREATE TABLE Customer (
    customer_id VARCHAR(10) NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    birthday DATE NOT NULL,
    certification_type VARCHAR(10) NOT NULL,
    id_number INT NOT NULL,
    password VARCHAR(20) NOT NULL
);


CREATE TABLE CustomerHistory(
    from_customer_id VARCHAR(10) NOT NULL,
    login_date DATE,
    login_time VARCHAR(10),
    FOREIGN KEY (from_customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Frequent_contact(
    from_customer_id VARCHAR(10),
    to_customer_id VARCHAR(10),
    last_transfer_date DATE,
    FOREIGN KEY (from_customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (to_customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Account(
    account_id VARCHAR(10) NOT NULL PRIMARY KEY,
    customer_id VARCHAR(10) NOT NULL,
    create_time DATE NOT NULL,
    currenct_type VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Investment_account(
    account_id VARCHAR(10) NOT NULL PRIMARY KEY,
    customer_id VARCHAR(10) NOT NULL,
    currency_type VARCHAR(20) NOT NULL,
    create_time DATE NOT NULL,
    total_value INT NOT NULL, 
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Saving_account(
    account_id VARCHAR(10) NOT NULL PRIMARY KEY,
    customer_id VARCHAR(10) NOT NULL,
    currency_type VARCHAR(20) NOT NULL,
    create_time DATE NOT NULL,
    balance INT NOT NULL, 
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Credit_account(
    account_id VARCHAR(10) NOT NULL PRIMARY KEY,
    customer_id VARCHAR(10) NOT NULL,
    currency_type VARCHAR(20) NOT NULL,
    create_time DATE NOT NULL,
    total_debt INT NOT NULL, 
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Transaction(
    transaction_id VARCHAR(10) NOT NULL PRIMARY KEY,
    in_account_id VARCHAR(10) NOT NULL,
    out_account_id VARCHAR(10) NOT NULL,
    in_consumer_id VARCHAR(10) NOT NULL,
    out_consumer_id VARCHAR(10) NOT NULL,
    amount INT NOT NULL,
    timepoint_date DATE NOT NULL,
    timepoint_time TIME NOT NULL,
    FOREIGN KEY (in_consumer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (out_consumer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (in_account_id) REFERENCES Account(account_id),
    FOREIGN KEY (out_account_id) REFERENCES Account(account_id)
);

CREATE TABLE Product(
    product_id VARCHAR(10) NOT NULL PRIMARY KEY,
    type VARCHAR(10) NOT NULL,
    price INT NOT NULL,
    holdings VARCHAR(20) NOT NULL,
    issuer VARCHAR(20) NOT NULL
);

-- interest_rate is stored in integer, during calculation it should be divided by 1000
CREATE TABLE Loan(
    loan_id VARCHAR(10) NOT NULL PRIMARY KEY,
    interest_rate INT NOT NULL
);

CREATE TABLE Product_contain(
    product_id VARCHAR(10) NOT NULL,
    account_id VARCHAR(10) NOT NULL,
    holdings VARCHAR(20) NOT NULL,
    product_values INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Product(product_id),
    FOREIGN KEY (account_id) REFERENCES Investment_account(account_id)
);

CREATE TABLE Loan_contain(
    loan_id VARCHAR(10) NOT NULL,
    account_id VARCHAR(10) NOT NULL,
    borrow_time DATE NOT NULL,
    next_due_time DATE NOT NULL,
    unpaid_amount INT NOT NULL,
    FOREIGN KEY (loan_id) REFERENCES Loan(loan_id),
    FOREIGN KEY (account_id) REFERENCES Credit_account(account_id)
);