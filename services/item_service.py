from database.connection import get_db_connection

def fetch_items_from_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM items")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        return {"error": str(e)}
    
def fetch_single_item_from_db(item_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM items WHERE item_id = %s"
        cursor.execute(sql, (item_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result is None:
         return {"error": "Item not found"}
        return result
    except Exception as e:
        return {"error": str(e)}
    


def add_item_to_db(item_data):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO items (item_name, category, price, stock_quantity) VALUES (%s, %s, %s, %s)"
        values = (item_data.item_name, item_data.category, item_data.price, item_data.stock_quantity)
        cursor.execute(sql, values)
        conn.commit()
        new_item_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return {"message": "Item created successfully", "item_id": new_item_id}
    except Exception as e:
        return {"error": str(e)}