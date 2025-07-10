from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def build_vectorstore(text):
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    return {'index': index, 'chunks': chunks, 'embeddings': embeddings}

def answer_question(vectorstore, question):
    q_embedding = model.encode([question])[0]
    D, I = vectorstore['index'].search(np.array([q_embedding]), k=1)
    if I[0][0] < len(vectorstore['chunks']):
        return vectorstore['chunks'][I[0][0]]
    else:
        return "Sorry, I couldn't find a relevant answer."
