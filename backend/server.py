from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel
from typing import List
import uuid

from backend.db_helper import *
from pyreusables.utilities import pylogger as logger


class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date


app = FastAPI()


@app.middleware("http")
async def logging_context(request, call_next):
    rid = str(uuid.uuid4())

    rid_token = logger.request_id.set(rid)
    pipe_token = logger.pipeline.set("expense_api")

    try:
        response = await call_next(request)
        return response
    finally:
        logger.request_id.reset(rid_token)
        logger.pipeline.reset(pipe_token)


@app.get("/expenses/add_update/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    logger.info("Fetching expenses", route=f"/expenses/{expense_date}", date=str(expense_date))
    expense = fetch_expenses_for_date(str(expense_date))

    logger.info("Expenses fetched", route=f"/expenses/{expense_date}", count=len(expense))
    return expense


@app.post("/expenses/add_update/{expense_date}")
def add_or_update_expenses(expense_date: date, expenses: List[Expense]):
    logger.info("Updating expenses", route=f"/expenses/{expense_date}", date=str(expense_date), count=len(expenses))

    delete_expenses_for_date(str(expense_date))
    for expense in expenses:
        insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Expenses added/updated successfully"}



@app.post("/expenses/analytics/")
def get_analytics(date_range: DateRange):
    break_down = {}

    data = fetch_expense_summary(str(date_range.start_date), str(date_range.end_date))

    total_amount = sum(item['total'] for item in data)
    for row in data:
        percentage = (row['total'] / total_amount) * 100 if total_amount != 0 else 0
        
        break_down[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }

    return break_down