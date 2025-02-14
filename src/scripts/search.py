import os
import sys
from dotenv import load_dotenv, find_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory.buffer import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

_ = load_dotenv(find_dotenv())


model = 'smollm2'
persist_directory = 'docs/chroma/'
embedding = OllamaEmbeddings(model=model)

def load_document(document):
    loader = PyPDFLoader(document)
    pages = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=150
    )
    pdf_docs = text_splitter.split_documents(pages)
    vectordb = Chroma.from_documents(
        documents=pdf_docs,
        embedding=embedding,
        persist_directory=persist_directory
    )
    
vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding,
)

llm = ChatOllama(temprature=0.6, model=model)
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)
retriever=vectordb.as_retriever()

qa = ConversationalRetrievalChain.from_llm(
    llm,
    retriever=retriever,
    memory=memory
)

# # Build prompt
# template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
# {context}
# Question: {question}
# Helpful Answer:"""
# QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

# qa_chain = RetrievalQA.from_chain_type(
#     llm,
#     retriever=vectordb.as_retriever(),
#     return_source_documents=True,
#     chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
# )

if __name__ == "__main__":
    if len(sys.argv) > 1:
        document = sys.argv[1]
        load_document(document)
    print("Welcome, I am ready to answer your queries")
    question = "say hello to the user"
    while True:
        question = input(">>> ")
        if question in ["q", "quit"]:
            break
        result = qa.invoke({"question": question })
        print(f">>> {result['answer']}")
