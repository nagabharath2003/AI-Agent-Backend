# tools/calculator.py
import math

def tool_calculate(expression: str) -> dict:
    """Safely evaluate a math expression."""
    try:
        result = eval(expression, {"__builtins__": None}, {"math": math})
        return {"result": result}
    except Exception as e:
        return {"error": f"Invalid expression: {str(e)}"}
