import os
import chromadb
import json
from langchain_community.embeddings import OpenAIEmbeddings 
from dotenv import load_dotenv

load_dotenv()

# Initialize Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

# Initialize OpenAIEmbeddings (can use other embeddings too)
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

#load the product, policy and questions/answers data
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

products = load_data('data/product_data.json')
policies = load_data('data/policies.json')
questions_answers = load_data('data/questions_answers.json')

# create a chroma collection
collection = client.get_or_create_collection(name=os.getenv("COLLECTION_NAME"))

documents = []
metadatas = []


# Add product data to the collection
for product in products:
    documents.append(str(product))
    metadatas.append(product)

# Add policy data to the collection
for policy in policies:
    documents.append(str(policy))
    metadatas.append(policy)

# Add question/answer data to the collection
for qa in questions_answers:
    documents.append(str(qa))
    metadatas.append(qa)

# Add data to the Chroma collection
try:
    collection.add(
        documents=documents,
        metadatas=metadatas,
        embeddings=[embeddings.embed_query(doc) for doc in documents],  # Ensure embeddings are in the correct format
        ids=[str(i) for i in range(len(documents))]
    )
    print("Data added to collection successfully.")
except Exception as e:
    print(f"\nError adding data to collection: {e}")
