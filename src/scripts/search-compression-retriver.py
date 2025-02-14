import os
import sys
from dotenv import load_dotenv, find_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

_ = load_dotenv(find_dotenv())

model = 'llama3.2'
persist_directory = 'docs/chroma/'

embedding = OllamaEmbeddings(model=model)
vectordb = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding,
)

llm = ChatOllama(temprature=0.8, model=model)
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectordb.as_retriever(search_type="mmr")
)

if __name__ == "__main__":
    question = sys.argv[1]
    results = compression_retriever.invoke(question)
    print(f"\n{'-' * 50}\n".join([f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(results)]))
