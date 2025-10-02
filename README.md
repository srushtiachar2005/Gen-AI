# Gen-AI Notes

1. Generative AI (Gen AI):
  • AI that creates content: text, images, audio, code
  • Uses LLMs like GPT, LLaMA, Claude
  • Tasks: text completion, Q&A, summarization, translation

2. LangChain:
  • Framework to build apps with LLMs
  • Connects models, prompts, memory, tools, agents
  • Use-cases: chatbots, QA systems, summarizers, RAG pipelines

3. LangChain Components:
  • Models: LLMs generating outputs
    • Chat: GPT-4, Claude
    • Text: GPT-3, LLaMA
    • Embedding: text-embedding-3
  • Prompts: Templates guiding output
  • Memory: Stores context (Buffer, Window, Summary)
  • Tools: Functions/APIs LLMs can call
  • Agents: LLM + memory + tools, makes decisions
  • Chains: Multi-step sequences for output generation

=> Gen AI Models:

  A. Language Models (LMs):
    • Purpose: Generate or understand human-like text
    • Examples: GPT-4, LLaMA, Claude, TinyLlama
    • Tasks: Chatbots, Q&A, summarization, translation, content generation
    • Types:
      • Open-Source: LLaMA, GPT-J, Falcon (can modify/use freely)
      • Closed-Source: GPT-4, Claude (proprietary, limited access)

  B. Embedding Models:
    • Purpose: Convert text/data into numerical vectors for analysis
    • Examples: text-embedding-3, all-MiniLM-L6-v2
    • Tasks: Semantic search, clustering, recommendation, similarity comparison
    • Types:
      • Open-Source: all-MiniLM-L6-v2, SBERT models
      • Closed-Source: text-embedding-3 (OpenAI), Cohere embeddings
