# tools/memory.py
from Database import get_db_cursor

def tool_save_memory(key: str, value: str) -> dict:
    """Save or update memory in database."""
    with get_db_cursor(commit=True) as cursor:
        if cursor:
            cursor.execute(
                "INSERT INTO memory (`key`, `value`) VALUES (%s, %s) "
                "ON DUPLICATE KEY UPDATE `value` = VALUES(`value`)",
                (key, value)
            )
            return {"status": "saved", "key": key, "value": value}
    return {"error": "Failed to save memory"}

def tool_get_memory(key: str) -> dict:
    """Retrieve memory from database."""
    with get_db_cursor() as cursor:
        if cursor:
            cursor.execute("SELECT `value` FROM memory WHERE `key` = %s", (key,))
            row = cursor.fetchone()
            if row:
                return {"key": key, "value": row["value"]}
            else:
                return {"error": f"No memory found for '{key}'"}
    return {"error": "Failed to fetch memory"}


'''if __name__ == "__main__":
    print("Testing Memory Tool...\n")

    # Test saving memory
    save_result = tool_save_memory("cat", "Fluffy")
    print("Save Result:", save_result)

    get_result = tool_get_memory("cat")
    print("Get Result:", get_result) '''
