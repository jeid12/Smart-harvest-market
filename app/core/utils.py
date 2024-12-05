from bson import ObjectId

# Utility function to convert MongoDB ObjectId to string
def object_id_to_str(obj_id):
    return str(obj_id)

# Utility function to check and convert string to MongoDB ObjectId
def str_to_object_id(obj_id_str):
    if ObjectId.is_valid(obj_id_str):
        return ObjectId(obj_id_str)
    raise ValueError("Invalid ObjectId string")
