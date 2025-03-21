import pymongo
from datetime import datetime


class Database:
  def __init__(self):
    self.client = pymongo.MongoClient("mongodb://localhost:27017")
    self.db = self.client["gpt_open_robot"]
    
    self.users_collection = self.db["users"]
    self.chats_collection = self.db["chats"]
    self.messages_collection = self.db["messages"]
    
  def check_is_user_exists(self, user_id: int) -> bool:
    if self.users_collection.count_documents({"_id": user_id}) > 0:
      return True
    else:
      return False
    
  def create_new_user(
    self,
    user_id: int,
    username: str = "",
    first_name: str = "",
    last_name: str = "",
    language_code: str = "en",
  ):
    new_user_data = {
      "_id": user_id,
      
      "username": username,
      "first_name": first_name,
      "last_name": last_name,
      
      "language_code": language_code,
      
      "created_at": datetime.now(),
      "last_active": datetime.now()
    }
    
    if not self.check_is_user_exists(user_id):
      self.users_collection.insert_one(new_user_data) 