import chromadb
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

# Specify the collection name you want to delete
collection_name = os.getenv("COLLECTION_NAME")

# Delete the collection
client.delete_collection(collection_name)

print(f"\nCollection '{collection_name}' deleted successfully.")


print(f"Remaining collections: {len(client.list_collections())}:\n {client.list_collections()}")