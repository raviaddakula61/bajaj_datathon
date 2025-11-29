from pydantic import BaseModel
from typing import List


class LineItem(BaseModel):
    description: str
    category: str
    quantity: str
    unit_price: str
    amount: str


class InvoiceResponse(BaseModel):
    bill_id: str
    patient_details: dict
    hospital_details: dict
    line_items: List[LineItem]
    printed_total: float
    sub_total: float
    discount: float
    tax: float
    final_total: float
    currency: str
    fraud_flags: list
