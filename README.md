# RAGnify — AI-Powered Document Chatbot for Apple 10-K Reports

**RAGnify** is a Retrieval-Augmented Generation (RAG) application that allows users to ask questions about Apple's 10-K annual report in simple, natural language. Instead of manually searching through a lengthy financial document, users can ask questions and receive relevant answers generated using document retrieval and Generative AI.

Built with **Python, Flask, FAISS, Hugging Face embeddings, and Google's Gemini API**, RAGnify transforms a static PDF into an interactive knowledge assistant.

## 🎯 Problem It Solves

Reading and understanding large PDF documents can be time-consuming and difficult. RAGnify helps solve these problems:

- **Time-consuming searches:** Users don't need to spend a lot of time searching through hundreds of pages to find specific information.
- **Difficult to understand:** Users can ask questions in simple English instead of trying to understand complex financial language.
- **Finding relevant information:** The system identifies document sections related to the user's question.
- **Manual reading effort:** Users can get a concise answer without reading the entire report.
- **Difficulty exploring financial reports:** Users can ask questions about Apple's business, financial performance, risks, and other information covered in the report.
- **Repeated information searches:** Users can retrieve relevant information by asking different questions instead of repeatedly searching the PDF manually.

## 🌍 Where Is It Mainly Used?

RAGnify demonstrates a document-question-answering approach that can be useful in several areas:

- **Finance and Investment Research:** Exploring annual reports, company performance, business risks, and financial disclosures.
- **Business Analysis:** Finding information about a company's operations, strategies, and reported results.
- **Education and Research:** Helping students and researchers understand lengthy reports and study materials.
- **Corporate Document Search:** Finding information in company reports, policies, manuals, and internal documentation.
- **Legal and Compliance Research:** Searching lengthy regulations, policies, and legal documents for relevant information. Important findings still require verification against the original source.
- **Customer and Employee Support:** Building knowledge assistants that answer questions using approved documentation.

*Current project scope: RAGnify uses Apple's 10-K report as its source document. The other use cases describe how this approach could be extended.*

## ✨ Key Features

- **PDF Document Processing:** Extracts text from Apple's 10-K annual report.
- **Intelligent Text Chunking:** Splits lengthy documents into smaller, manageable text segments.
- **Semantic Search:** Uses Hugging Face embeddings to find relevant content based on meaning.
- **FAISS Vector Search:** Retrieves relevant document chunks efficiently through vector similarity search.
- **Generative AI Responses:** Uses Google's Gemini API to generate natural-language answers based on retrieved document context.
- **Flask Backend API:** Provides endpoints for processing questions and returning responses.
- **Reusable Document Pipeline:** Separates document ingestion and indexing from question-answering.

## 🛠️ Technology Stack

- **Programming Language:** Python
- **Backend Framework:** Flask
- **API and Data Format:** REST API, JSON
- **API Testing:** Postman
- **LLM Provider:** Google Gemini API
- **Embeddings:** Hugging Face Sentence Transformers
- **Vector Search:** FAISS
- **Document Processing:** PyPDF / PyPDFLoader
- **Text Splitting:** LangChain Text Splitters

## 🔄 How It Works

1. **Document Ingestion:** Load and extract text from the Apple 10-K PDF.
2. **Text Chunking:** Divide the extracted text into smaller, overlapping chunks.
3. **Embedding Generation:** Convert text chunks into vector representations using an embedding model.
4. **Vector Indexing:** Store the embeddings in a FAISS index for similarity-based retrieval.
5. **Question Processing:** Receive a user's natural-language question through the Flask API.
6. **Context Retrieval:** Retrieve document chunks relevant to the question.
7. **Answer Generation:** Send the question and retrieved context to Gemini to generate a relevant answer.

## 🚀 Future Enhancements

- Conversational chat history
- User authentication and session management
- MySQL integration for users and chat history
- Improved error handling and document-processing validation
- A web-based chat interface

## 💡 Key Learning Outcomes

This project provides hands-on experience with RAG architecture, semantic search, vector embeddings, FAISS indexing, LLM integration, document processing, and REST API development using Flask.

**RAGnify — Turning lengthy documents into knowledge you can interact with.**
