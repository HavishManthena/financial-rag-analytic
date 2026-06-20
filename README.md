# 📈 Financial Earnings Report RAG System

A lightweight Retrieval-Augmented Generation (RAG) pipeline designed to parse, index, and query unstructured corporate data from earnings reports using `LlamaIndex` and local vector search optimization.

## ⚡ Key Architecture
- **In-Memory Tokenizer:** Parses raw data structures placed directly inside the local path directory.
- **Persistent Local Index:** Serializes vector metrics embeddings locally to dramatically reduce repetitive inference processing fees.
- **Context Grounding Matrix:** Restricts the language model from hallucinating by anchoring generated answers directly to retrieved semantic arrays.

## 🛠️ Execution Pipeline Instructions

1. **Clone project structures locally:**
   ```bash
   git clone [https://github.com/HavishManthena/financial-rag-analytic.git](https://github.com/HavishManthena/financial-rag-analytic.git)
   cd financial-rag-analytic
   pip install -r requirements.txt
   export OPENAI_API_KEY="your-actual-api-key-here"
   python app.py
   
   
