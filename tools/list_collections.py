import chromadb


# Initialize the Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

print(f"Collections: {len(client.list_collections())}\n {client.list_collections()}")