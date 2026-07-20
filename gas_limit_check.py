def validate_gas_limit(limit):
    min_limit = 21000
    max_limit = 30000000
    return min_limit <= limit <= max_limit

print(f"Is gas limit valid (50000): {validate_gas_limit(50000)}")
