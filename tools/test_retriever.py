import os
import chromadb
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

client = chromadb.PersistentClient(path="./chroma_db")

# Initialize OpenAI embeddings
# embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

# # Create a Chroma collection with the embeddings
# vectorstore = Chroma(
#     client=client,
#     collection_name=os.getenv("COLLECTION_NAME"),
#     embedding_function=embeddings
# )

# # Verify that the collection is created correctly
# print("Vector store created:", vectorstore.embeddings)

collection = client.get_collection(os.getenv("COLLECTION_NAME"))
print(collection)