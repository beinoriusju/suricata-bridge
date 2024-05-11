def fix_keys(data):
    if isinstance(data, dict):
        # Create a new dictionary with dots replaced in keys
        modified_dict = {k.replace('.', '_'): fix_keys(v) for k, v in data.items()}
        return modified_dict
    elif isinstance(data, list):
        # Process each item in the list recursively
        return [fix_keys(item) for item in data]
    else:
        # Return the item as is if it's not a dictionary or list
        return data