def to_float(val):
    try:
        return float(val)
    except ValueError:
        return None  # or replace with some default value like 0 or np.nan