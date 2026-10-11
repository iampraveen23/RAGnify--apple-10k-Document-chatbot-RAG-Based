# RAGnify — AI-Powered Document Chatbot for Apple 10-K Reports

**RAGnify** is a Retrieval-Augmented Generation (RAG) application that allows users to ask questions about Apple's 10-K annual report using natural language. Instead of manually searching through a lengthy PDF, users can ask questions and receive relevant answers generated using document retrieval and Generative AI.

Built with **Python, Flask, FAISS, Hugging Face embeddings, and Google's Gemini API**, RAGnify transforms a static PDF into an interactive knowledge assistant.

**Current Project Focus:** As of now, RAGnify mainly focuses on the **backend**, including PDF processing, text chunking, embedding generation, vector search, API development, and LLM integration. A complete frontend interface can be added in a future phase.

## 🎯 Problem It Solves

Reading and searching through large documents can take a lot of time. RAGnify aims to make this process easier.

- **Time-consuming document searches:** Users don't have to manually search through every page to find relevant information.
- **Difficulty understanding large documents:** Users can ask questions in simple English instead of searching for exact keywords.
- **Information spread across many pages:** The system retrieves relevant text chunks from the document to help answer a question.
- **Keyword search limitations:** Semantic search can find relevant information based on meaning, even when the question uses different words from the document.
- **Finding answers from lengthy reports:** Users can ask questions about the Apple 10-K report and receive answers based on the retrieved document context.
- **Reducing unsupported answers:** Providing relevant document context to the language model helps ground its responses in the source material, although answers should still be verified.

## 🌍 Where Is RAGnify Mainly Used?

RAGnify demonstrates a document-question-answering approach that can be applied in several areas:

- **Finance and Business:** Exploring annual reports, financial statements, company reports, and business documents.
- **Education and Research:** Finding information in textbooks, research papers, study materials, and academic PDFs.
- **Corporate Knowledge Management:** Helping employees search internal documentation, policies, and company manuals.
- **Legal Document Analysis:** Finding relevant information in contracts, policies, and legal documents. Important conclusions still require professional review.
- **Technical Documentation:** Searching software manuals, API documentation, and technical guides.
- **Customer Support:** Helping support teams retrieve relevant information from product manuals and knowledge-base documents.

*Currently, the project uses Apple's 10-K report as its sample document. The other use cases describe potential applications that could be supported through future extensions.*

## ✨ Key Features

- **PDF Document Processing:** Extracts text from Apple's 10-K annual report.
- **Intelligent Text Chunking:** Splits lengthy documents into smaller, manageable text segments.
- **Text Embeddings:** Converts document chunks into numerical representations using Hugging Face Sentence Transformers.
- **Semantic Search:** Finds document content based on meaning rather than exact keyword matches.
- **FAISS Vector Search:** Retrieves relevant document chunks using vector similarity search.
- **Generative AI Responses:** Uses Google's Gemini API to generate natural-language answers based on retrieved context.
- **Flask Backend API:** Accepts questions through API endpoints and returns responses.
- **Modular Processing Pipeline:** Separates document ingestion and indexing from question-answering.

## 🛠️ Technology Stack

- **Programming Language:** Python
- **Backend Framework:** Flask
- **API Development:** REST API and JSON
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
4. **Vector Indexing:** Store the embeddings in a FAISS index for efficient similarity search.
5. **Question Processing:** Accept a user's natural-language question through the Flask backend API.
6. **Context Retrieval:** Retrieve relevant document chunks using semantic similarity search.
7. **Answer Generation:** Send the question and retrieved context to Gemini to generate a relevant answer.
8. **API Response:** Return the generated answer through the backend API.

## 🎯 Project Objective

The objective of RAGnify is to demonstrate how Retrieval-Augmented Generation can make large documents easier to explore. The project combines document processing, vector search, embeddings, REST API development, and large language models into a practical Generative AI backend application.

## 🚀 Future Enhancements

- Conversational chat history.
- MySQL integration for storing user information and chat history.
- Improved error handling and document-processing validation.
- A web-based chat interface for an improved user experience.

## 💡 Key Learning Outcomes

- Understanding the Retrieval-Augmented Generation (RAG) architecture.
- Working with PDF document loading and text chunking.
- Generating and searching vector embeddings.
- Building a Flask backend and REST API.
- Integrating an external LLM API.
- Testing API endpoints using Postman.
- Understanding how document retrieval and LLMs work together.

**RAGnify — Turning lengthy documents into information users can ask questions about.**
