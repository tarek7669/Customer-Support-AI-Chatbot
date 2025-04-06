from langchain.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI Embeddings with your API key
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Sample text to embed (you can replace this with any document or string)
sample_text = ["This is a test sentence to check the embedding dimensionality."]

# Get the embedding for the sample text
embedding = embeddings.embed_documents(sample_text)[0]

# Check the dimensionality of the embedding
dimensionality = len(embedding)

print(f"The dimensionality of the embedding is: {dimensionality}")
