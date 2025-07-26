import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()
api_key = os.getenv("groq_api")  # Ensure your .env has: groq_api=your_key_here

# Step 1: Load entire PDF (even 100+ pages)
loader = PyPDFLoader("data/sample.pdf")
docs = loader.load()

# Step 2: Split PDF into chunks optimized for long texts
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
chunks = splitter.split_documents(docs)

# Step 3: Convert text to embeddings and index with FAISS
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(chunks, embedding)
retriever = vectorstore.as_retriever()

# Step 4: Set up LLM (Groq with LLaMA3)
llm = ChatGroq(api_key=api_key, model_name="llama3-70b-8192")

# Step 5: Create QA Chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Step 6: Ask questions in a loop
print("\n📄 PDF loaded successfully. Ask me anything about it!\n")
while True:
    question = input("❓ Ask a question (type 'exit' to quit): ")
    if question.lower().strip() == "exit":
        print("👋 Exiting. Have a great day!")
        break
    try:
        response = qa_chain.invoke({"query": question})
        print("\n🧠 Answer:", response['result'].strip(), "\n")
    except Exception as e:
        print("⚠️ Error:", str(e))
