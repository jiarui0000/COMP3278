**Customer** ( *customer_id*, name, gender, birthday, authentication.certification_type, authentication.id_number, password)

foreign key: none


**CustomerHistory** ( *customer_id*, login_date, login_time)

foreign key: 

  *customer_id* REFERENCES **Customer**[from]


**Frequent_contact** ( *customer_id*, *customer_id*, last_transfer_date)

foreign key: 

​	*customer_id* REFERENCES **Customer**[from]

​	*customer_id* REFERENCES **Customer**[to]

**Account** (*customer_id*, *account_id*, create_time, current_type)

foreign key:

​	*customer_id* REFERENCES **Customer**

**Investment_account** ( *customer_id*, *account_id*, currency_type, create_time, total_value)

foreign key: 

​	*customer_id* REFERENCES **Customer **

**Saving_account** ( *customer_id*, *account_id*, currency_type, create_time, balance)

foreign key: 

​	*customer_id* REFERENCES **Customer **

**Credit_account** ( *customer_id*, *account_id*, currency_type, create_time, total_debt)

foreign key: 

​	*customer_id* REFERENCES **Customer **

**Transaction** ( *account_id (in)*, *account_id (out)*, *customer_id (in)*, *customer_id (out)*, *transaction_id*, amount, timepoint.date, timepoint.time)

foreign key: 

​	*customer_id (in)* REFERENCES **Customer**[form]

​	*customer_id (our)* REFERENCES **Customer**[to]

​	*account_id (in)* REFERENCES **Account**[from]

​	*account_id (out)* REFERENCES **Account**[to]

**Product** ( *product_id*, type, price, holdings, issuer)

foreign key: none

**Loan** ( *loan_id*, interest_rate)

foreign key: none

**Product_contain** ( *product_id*, *account_id*, holdings, values)

foreign key:

​	*product_id* REFERENCES **Product**

​	*account_id* REFERENCES **Investment_account**

**Loan_contain** ( *loan_id*, *account_id*, borrow_time, next_due_date, unpaid_amount)

foreign key:

​	*loan_id* REFERENCES **Loan**

​	*account_id* REFERENCES **Credit_account**
