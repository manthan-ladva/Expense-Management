import pandas as pd
import json
import logging

from pyreusables.pydatabase import factory



db = factory.database_factory('mysql', 'local')



def fetch_expenses_for_date(expense_date):
    rows, cols = db.fetch("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
    return [dict(zip(cols, row)) for row in rows]


def delete_expenses_for_date(expense_date):
    _ = db.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def insert_expense(expense_date, amount, category, notes):
    db.insert_bulk(
        table="expenses", 
        rows=[(expense_date, amount, category, notes)], 
        columns=["expense_date", "amount", "category", "notes"]
    )


def fetch_expense_summary(start_date, end_date):
    query = '''SELECT category, SUM(amount) as total 
           FROM expenses WHERE expense_date
           BETWEEN '{}' and '{}' 
           GROUP BY category;'''.format(start_date, end_date)
    
    rows, cols = db.fetch(query)
    return [dict(zip(cols, row)) for row in rows]



if __name__ == "__main__":
    a  = fetch_expense_summary('2024-08-01', '2025-08-05')
    print("Done")
    print(a)