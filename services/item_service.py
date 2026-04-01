from database.connection import get_db_connection

# Helpers 
def execute_read_query(sql: str, values: tuple = None, fetch_one: bool = False):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) # Give me nice JSON-like data!
    
    if values:
        cursor.execute(sql, values)
    else:
        cursor.execute(sql)
        
    if fetch_one:
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()
        
    cursor.close()
    conn.close()
    return result



def execute_write_query(sql: str, values: tuple = None):
    conn = get_db_connection()
    cursor = conn.cursor() # No dictionary needed here
    
    if values:
        cursor.execute(sql, values)
    else:
        cursor.execute(sql)
        
    conn.commit() # Save the changes!
    rows_affected = cursor.rowcount
    last_insert_id = cursor.lastrowid

    
    cursor.close()
    conn.close()
    return rows_affected, last_insert_id





# services
def fetch_items_from_db():
    try:
        sql = "SELECT * FROM items"
        result = execute_read_query(sql)
        if result is None:
            return {"error": "There's no item in the Table."}
        return result
    except Exception as e:
        return {"error": str(e)}
    


def fetch_single_item_from_db(item_id: int):
    try:
        sql = "SELECT * FROM items WHERE item_id = %s"
        result = execute_read_query(sql, (item_id,), fetch_one=True)

        if result is None:
            return {"error": "Item not found Please check the ID and try again."}
        return result
    except Exception as e:
        print(f"Internal Database Error {e}")
        return {"error": "Oops! Something went wrong on our end. Please try again Later."}
    


def add_item_to_db(item_data):
    try:
        sql = "INSERT INTO items (item_name, category, price, stock_quantity) VALUES (%s, %s, %s, %s)"
        values = (
            item_data.item_name,
            item_data.category,
            item_data.price,
            item_data.stock_quantity
        )
        rows_affected, new_item_id = execute_write_query(sql, values)
        return {"message": "Item created successfully", "item_id": new_item_id}
    except Exception as e:
        return {"error": str(e)}



def update_item_in_db(item_id, item_data):
    try:
        sql = "UPDATE items SET item_name = %s, category = %s, price = %s, stock_quantity = %s WHERE item_id = %s"
        values = (
            item_data.item_name,
            item_data.category,
            item_data.price,
            item_data.stock_quantity,
            item_id
        )
        rows_affected, _ = execute_write_query(sql, values)
        if rows_affected == 0:
            return {"message": "Item not found or no new changes made"}
        return  {"message": "Item updated succesfully"}
    except Exception as e:
        print(f"Internal Database Error: {e}")
        return {"error": "Oops! Something went wrong on our end. Please try again Later."}
    


def remove_item_from_db(item_id):
    try:
        sql = "DELETE FROM items WHERE item_id = %s"
        rows_affected, _ = execute_write_query(sql, (item_id,),)

        if rows_affected == 0:
            return {"error": "Item not found. Could not delete."}
        return {"message": "Item deleted succesfully."}
    except Exception as e:
        print(f"Internal Database Error: {e}")
        return {"error": "Oops! Something went wrong while deleting the item."}