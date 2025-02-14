import os
import sys
from dotenv import load_dotenv, find_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

_ = load_dotenv(find_dotenv())

model = 'llama3.2'
persist_directory = 'docs/chroma/'

embedding = OllamaEmbeddings(model=model)
vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding,
)

llm = ChatOllama(temprature=0.6, model=model)

# Build prompt
template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
{context}
Question: {question}
Helpful Answer:"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

if __name__ == "__main__":
    question = sys.argv[1]
    result = qa_chain.invoke({"query": question })
    print(result['result'])
