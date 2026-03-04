Slowly-changing dimensions are modeled incorrectly so much! 

There are 4 types:

- Type 0 
These dimensions aren't slowly changing. They are fixed. Think of things like birth date or sign-up date. 

- Type 1 
This is the worst way to model your slowly changing dimensions. You naively update the table with the most recent value. This destroys the historical integrity of the table!

- Type 2 
This is the golden standard for modeling slowly changing dimensions but also the most complicated. You add a new row to the table every time the value changes with the date range it is valid

- Type 3
This is one is a tradeoff where you store the previous value and current value in one row. It maintains some historical integrity but not perfect integrity like Type 2


How do you like to model your slowly changing dimensions?

Credits: learn.dataexpert.io 
