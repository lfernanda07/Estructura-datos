def validate_customer_data(customer_data):
    if not isinstance(customer_data, dict):
        raise ValueError("Customer data must be a dictionary.")
    
    required_fields = ["name", "account_number", "priority"]
    for field in required_fields:
        if field not in customer_data:
            raise ValueError(f"Missing required field: {field}")

def assign_priority(customer_data):
    priority_mapping = {
        "high": 1,
        "medium": 2,
        "low": 3
    }
    return priority_mapping.get(customer_data.get("priority", "low"), 3)