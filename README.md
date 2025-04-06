# **Customer Support AI Agent**  

## Overview  
The Customer Support AI Agent is a customer support assistant that helps answer questions about electronic products, store policies, and FAQs. It leverages OpenAI's GPT-4o-mini model and Langchain tool along with a ChromaDB-powered knowledge base to provide accurate and informative responses.  

## Project Structure  
```
Customer Support AI Agent
│── chroma_db/                     # Automatically created database directory (do not modify manually)
│── data/
│   ├── product_data.json          # Contains product details
│   ├── policies.json              # Contains store policies
│   ├── questions_answers.json     # Contains example Q&A pairs
│── examples/                      # Contains example conversations showing the agent in action
│── tools/
│   ├── list_collections.py        # Lists existing ChromaDB collections
│   ├── delete_collection.py       # Deletes a specific ChromaDB collection
│── .env                           # Stores environment variables (API keys & ChromaDB Collection Name)
│── Instructions.txt               # Instructions on how to setup and run the agent
│── knowledge_base.py              # Handles ChromaDB storage and retrieval
│── main.py                        # CLI interface to interact with the AI assistant
│── openai_agent.py                # AI agent logic (LLM + RetrievalQA)
│── README.md                      # Project explanation
│── requirements.txt               # Dependencies
```

## Approach  

### 1. Data Storage  
- JSON files store product information, policies, and FAQs.  
- ChromaDB is used as a vector database to store and retrieve relevant information.  

### 2. AI Model  
- Uses OpenAI's GPT-4o-mini via the OpenAI API for generating responses.  
- OpenAIEmbeddings are used to convert text data into vector representations.  

### 3. Retrieval Mechanism  
- The agent fetches relevant documents from ChromaDB using semantic search.  
- LangChain's `RetrievalQA` chain is used to process and generate responses.  

### 4. User Interaction  
- A CLI-based interface (`main.py`) allows users to interact with the AI agent by asking questions.  
- The AI responds with product-related answers using a **custom prompt template**.  

## Installation & Usage  

### Prerequisites  
- Python 3.12.9

### Setup  
1. Create a virtual environment and install dependencies:  
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

2. Run the AI assistant:  
```bash
python main.py
```
Then, start asking questions like:  
```
What are the features of UltraPhone X?
```

## Key Technologies Used
- **Python 3.12.9** – Core programming language.  
- **LangChain** – Framework for building LLM-powered applications, including retrieval-based question answering.  
- **OpenAI GPT-4o-mini** – Large language model used for generating responses.  
- **ChromaDB** – Vector database for storing and retrieving product and policy information.  
- **OpenAIEmbeddings** – For converting product data into embeddings  
- **OpenAI API** – Used for LLM queries and embeddings.  
- **dotenv** – Manages environment variables securely.
