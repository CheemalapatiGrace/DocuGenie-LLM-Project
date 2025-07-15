DocuGenie – Context Aware Document Assistant Using LLMs

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


Installation & Setup

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

DocuGenie leverages advanced prompt engineering techniques to dynamically generate prompts based on the context of uploaded documents, ensuring that interactions with the LLM remain relevant and coherent. It incorporates Retrieval-Augmented Generation (RAG) to ground responses in the source material, improving factual accuracy and reducing hallucinations. The system also includes robust file parsing capabilities using libraries that extract and normalize content from PDF, DOCX, and TXT formats. Additionally, semantic search can be integrated to improve the experience for users navigating long or complex documents by enabling more accurate information retrieval.

Use Cases

DocuGenie is suitable for a wide range of real-world applications. It can assist legal professionals in analyzing lengthy contracts and agreements, help researchers summarize academic papers, enable HR or compliance teams to interpret corporate policies, and support students in understanding and querying study materials. Its versatility and adaptability make it a powerful tool for any domain involving document-heavy workflows.
