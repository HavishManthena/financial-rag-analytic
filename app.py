import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

# Configure API authentication securely via environment tokens
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "your-fallback-key-for-local-testing")

PERSIST_DIR = "./storage"
DATA_DIR = "./financial_docs"

def initialize_rag_system():
    """Validates local environment variables and compiles/instantiates data stores."""
    # Ensure local ingestion directory exists securely
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        # Seed standard sample report parameters to prevent engine failures
        with open(os.path.join(DATA_DIR, "q3_report.txt"), "w") as f:
            f.write("Tesla Q3 2026 Financial Highlights:\n"
                    "- Total revenue grew to $26.1 billion, up 8% year-over-year.\n"
                    "- Net income was $2.3 billion.\n"
                    "- Free cash flow increased to $2.8 billion.\n"
                    "- Energy storage deployments reached a record 7.1 GWh.")

    # Conditional logic block separating new index creation vs processing cached vector logs
    if not os.path.exists(PERSIST_DIR):
        print("⚡ Parsing local financial telemetry data and constructing index store...")
        documents = SimpleDirectoryReader(DATA_DIR).load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        print("📁 Loading existing cached semantic database structures...")
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
        
    return index

if __name__ == "__main__":
    # Boot the primary data parsing infrastructure layers
    finance_index = initialize_rag_system()
    query_engine = finance_index.as_query_engine()
    
    # Execute a sample data verification tracking prompt
    query = "What was Tesla's total revenue in Q3 2026 and how much did it grow?"
    print(f"\nUser Query: {query}")
    
    response = query_engine.query(query)
    print(f"\nRAG AI Response:\n{response}")
