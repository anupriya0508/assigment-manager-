import pymongo

# MongoDB connection configuration
mongo_client = pymongo.MongoClient("mongodb+srv://mongo:mongopassword@assignment.ejkqc64.mongodb.net/?retryWrites=true&w=majority")  # Update the MongoDB connection string as needed
db = mongo_client["assignment_manager"]
assignments_collection = db["assignments"]
users_collection = db["users"]

def insert_assignment(assignment_data):
    """
    Insert a new assignment into the database.

    Args:
        assignment_data (dict): Assignment data to be inserted.

    Returns:
        str: The ObjectId of the inserted document.
    """
    result = assignments_collection.insert_one(assignment_data)
    return str(result.inserted_id)

def get_assignments():
    """
    Retrieve a list of all assignments from the database.

    Returns:
        list: List of assignment documents.
    """
    return list(assignments_collection.find())

def get_assignment_by_id(assignment_id):
    """
    Retrieve an assignment by its ObjectId from the database.

    Args:
        assignment_id (str): The ObjectId of the assignment document.

    Returns:
        dict: Assignment document.
    """
    return assignments_collection.find_one({"_id": pymongo.ObjectId(assignment_id)})

def insert_user(user_data):
    """
    Insert a new user into the database.

    Args:
        user_data (dict): User data to be inserted.

    Returns:
        str: The ObjectId of the inserted document.
    """
    result = users_collection.insert_one(user_data)
    return str(result.inserted_id)

def get_user_by_username(username):
    """
    Retrieve a user by their username from the database.

    Args:
        username (str): The username of the user.

    Returns:
        dict: User document.
    """
    return users_collection.find_one({"username": username})

def get_assignment_by_title(title):
    """
    Retrieve an assignment by its title from the database.

    Args:
        title (str): The title of the assignment.

    Returns:
        dict: Assignment document or None if not found.
    """
    return assignments_collection.find_one({"title": title})

