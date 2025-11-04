# utils.py
import re

def extract_calculation(prompt: str) -> str:
    """Extract a math expression from a prompt."""
    prompt = prompt.lower().replace("what is", "").replace("calculate", "").strip()
    prompt = (
        prompt.replace("plus", "+")
        .replace("minus", "-")
        .replace("times", "*")
        .replace("divided by", "/")
    )
    return prompt

def extract_memory_save(prompt: str):
    """Extract key-value pair for 'remember' or 'save' prompts."""
    # Example: "Remember my cat's name is Fluffy"
    prompt = prompt.lower().replace("remember", "").replace("save", "").strip()
    match = re.match(r"(.*) is (.*)", prompt)
    if match:
        key = match.group(1).strip()
        value = match.group(2).strip()
        return key, value
    return None, None

def extract_memory_get(prompt: str):
    """Extract key from 'what is my' or 'recall' prompts."""
    prompt = prompt.lower().replace("what is my", "").replace("recall", "").strip()
    return prompt
