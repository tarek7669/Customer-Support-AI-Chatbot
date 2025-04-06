import os
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma 
from langchain.prompts import PromptTemplate
import chromadb


# Load environment variables
load_dotenv()

# Initialize the Chroma client
client = chromadb.PersistentClient(path="./chroma_db")

# Load the knowledge base
collection = client.get_or_create_collection(os.getenv("COLLECTION_NAME"))

# Create the LLM using GPT-2
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

vectorstore = Chroma(
    client=client,
    collection_name=os.getenv("COLLECTION_NAME"),
    embedding_function=embeddings
)


# Define a LangChain PromptTemplate
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
            You are a helpful AI assistant specialized in answering customer inquiries about electronic products.
            You have access to a knowledge base that contains information about various products, policies, and frequently asked questions.
            Your task is to provide accurate and helpful responses to customer questions based on the information in the knowledge base.

            Use the following information to answer the question:

            {context}

            Customer Question: {question}

            Provide a concise and informative response.
            """
)

# Create the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    chain_type_kwargs={"prompt": prompt_template}
)

def get_agent_response(user_question):
    try:
        # Use the retrieval chain to fetch an answer
        response = qa_chain.invoke(user_question)
        return response.get("result")
    except Exception as e:
        return f"Error: {e}"