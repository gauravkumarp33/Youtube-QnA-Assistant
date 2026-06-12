from dotenv import load_dotenv 
from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings)
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS

load_dotenv()

embeddings_model= GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
llm= ChatGoogleGenerativeAI(model="gemini-2.5-flash")


def create_vectors(video_url:str) -> FAISS:
    loader= YoutubeLoader.from_youtube_url(video_url)
    documents= loader.load()

    splitter= RecursiveCharacterTextSplitter(
        chunk_size= 1000,
        chunk_overlap=100 )
    
    chunk= splitter.split_documents(documents)

    vector_store= FAISS.from_documents(
        documents=chunk,
        embedding= embeddings_model
    )

    return vector_store


def get_response(vector_store,query,k = 4):
    docs =  vector_store.similarity_search(query,k=k)
    docs_page_content = " ".join([doc.page_content for doc in docs])

    prompt = ChatPromptTemplate.from_template(
     """
        You are a helpful Youtube assistant who answers the user's question based on the given 
        transcript of the video. Use only the provided information to answer the question. 

        Answer the following question: {question}
        Using the relevant information from the transcript: {docs}

        give a concise and accurate answer to the question based on the provided information.

        and if you don't know the answer and if it is not in the transcript, say you don't know.
        """
    )
    rag_chain = prompt | llm | StrOutputParser() 
    raw_response = rag_chain.invoke({"question": query, "docs": docs_page_content})
    response= raw_response.replace("\n","").strip()
    return response, docs




