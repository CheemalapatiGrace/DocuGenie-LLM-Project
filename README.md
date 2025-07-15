#DocuGenie – Context Aware Document Assistant Using LLMs

DocuGenie is an intelligent, context aware document assistant powered by open source Large Language Models (LLMs). It allows users to upload documents in formats such as PDF, DOCX, and TXT, interact with the content using natural language queries, receive intelligent summaries, and verify the factual consistency of generated answers.

This project demonstrates best practices in prompt engineering, context management, and retrieval-augmented generation (RAG) to enhance document understanding and interaction.

Features

 Upload documents (PDF, DOCX, TXT)
 Ask natural language questions about the content
 Receive intelligent, context-aware answers
 Generate concise summaries of uploaded documents
 Evaluate factual consistency using retrieval-based validation
 Built with modular architecture for LLM integration
 
Tech Stack

| Category        | Technologies                                        |
| --------------- | --------------------------------------------------- |
| Frontend        | React.js, Tailwind CSS                              |
| Backend         | Node.js, Express.js                                 |
| LLM Integration | Open-source LLMs (e.g., GPT-J, GPT-NeoX), LangChain |
| File Handling   | PDF.js, mammoth.js, fs, docx-parser                 |
| NLP Operations  | Prompt engineering, RAG, semantic search            |
| Database        | PostgreSQL (or any supported alternative)           |
| Deployment      | Vercel (frontend), Render / Railway (backend)       |



Project Structure

DocuGenie/
├── client/                # Frontend (React)
├── server/                # Backend (Node.js, Express)
├── prompts/               # Prompt templates and examples
├── utils/                 # File parsers, formatters
├── docs/                  # Additional documentation
└── README.md

#Installation & Setup

1. Clone the Repository
git clone https://github.com/gracecheemalapati/docugenie.git
cd docugenie

2. Install Dependencies
Frontend

cd client
npm install
Backend

cd ../server
npm install

3. Run Locally
Start Backend

npm start
Start Frontend (in separate terminal)

npm run dev


Core Concepts

Prompt Engineering: Dynamic prompt generation based on document context.
Retrieval-Augmented Generation (RAG): Ensures factual accuracy by grounding responses in uploaded documents.
File Parsing: Uses libraries to extract structured content from multiple document formats.
Semantic Search (Optional): Can be integrated to enhance long document navigation and QA performance.

Use Cases

Legal document analysis
Research paper summarization
Corporate policy understanding
Academic study assistant

