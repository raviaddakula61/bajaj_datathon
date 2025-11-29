import json

def validate_totals(model_output: str):
    """
    Accepts raw JSON text from Groq and:
      - parses it
      - recalculates totals
      - adds fraud flags
      - returns consistent JSON
    """

    # 1. Convert JSON string → Python dict
    try:
        data = json.loads(model_output)
    except Exception:
        return {
            "error": "Model did not return valid JSON",
            "raw_output": model_output
        }

    # ---- 2. Extract line items ----
    items = data.get("line_items", [])
    subtotal = sum(float(i.get("amount", 0)) for i in items)

    data["sub_total"] = round(subtotal, 2)

    # ---- 3. Compute totals ----
    discount = float(data.get("discount", 0))
    tax = float(data.get("tax", 0))
    final_total = subtotal - discount + tax
    data["final_total"] = round(final_total, 2)

    # ---- 4. Fraud check ----
    fraud = []

    printed_total = float(data.get("printed_total", 0))
    if printed_total and abs(printed_total - subtotal) > 1:
        fraud.append("total_mismatch")

    data["fraud_flags"] = fraud
    return data
