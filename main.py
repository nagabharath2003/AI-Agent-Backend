from fastapi import FastAPI
from models import QueryRequest
from memory import tool_save_memory, tool_get_memory
from calculator import tool_calculate
from utils import extract_calculation, extract_memory_save, extract_memory_get
from Database import create_table

# Automatically create the table when app starts
create_table()


app = FastAPI(title="AI Agent Backend")

@app.post("/agent/query")
def agent_query(request: QueryRequest):
    prompt = request.prompt.lower()

    # Choose the tool based on prompt intent
    if "remember" in prompt or "save" in prompt:
        key, value = extract_memory_save(prompt)
        if key and value:
            response = tool_save_memory(key, value)
            chosen_tool = "memory_write"
            tool_input = f"{key}={value}"
        else:
            return {"error": "Could not parse save memory command."}

    elif "what is my" in prompt or "recall" in prompt:
        key = extract_memory_get(prompt)
        response = tool_get_memory(key)
        chosen_tool = "memory_read"
        tool_input = key

    elif "what is" in prompt or "calculate" in prompt:
        expression = extract_calculation(prompt)
        response = tool_calculate(expression)
        chosen_tool = "calculator"
        tool_input = expression

    else:
        return {"error": "I do not have a tool for that."}

    return {
        "original_prompt": request.prompt,
        "chosen_tool": chosen_tool,
        "tool_input": tool_input,
        "response": response
    }

