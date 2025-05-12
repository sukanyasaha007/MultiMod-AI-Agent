# 🔥 MultiMod-AI-Agent: Wildfire Detection Edition

A powerful multi-modal AI agent that fuses image and text analysis to identify and explain wildfire events using vision models and LLMs. Built to showcase advanced RAG pipelines and real-world AI applications on wildfire imagery.

---

## 📸 Dataset

Uses the **Wildfire Detection Image Data** from [Kaggle](https://www.kaggle.com/datasets/brsdincer/wildfire-detection-image-data), which contains:

- 🔥 Wildfire images
- 🌲 Non-wildfire images
- 📄 Optional accompanying documentation

---

## 💡 Key Features

- 🖼️ Analyze wildfire-related images using **CLIP** or **BLIP**
- 📄 Ingest related documents and reports (PDF, DOCX, TXT)
- 🧠 Use **RAG** (Retrieval-Augmented Generation) to answer natural language queries
- 💬 Ask multi-modal questions like:  
  - “Does this image show early or active wildfire stages?”  
  - “What containment strategy fits the scene in this image?”  
  - “Compare the document's advice with this visual situation”

---

## ⚙️ Tech Stack

| Component         | Technology                                      |
|------------------|--------------------------------------------------|
| Image Embedding  | CLIP / BLIP via HuggingFace Transformers         |
| Text Parsing     | PyMuPDF, python-docx, LangChain loaders          |
| Vector DB        | ChromaDB / PGVector / FAISS                      |
| LLM Reasoning    | LLaMA 3, GPT-4, or Mistral via LangChain         |
| UI               | Streamlit or FastAPI                             |
| Agent Framework  | LangChain (retrieval + reasoning + memory)       |

---

## 📁 Project Structure
```bash
MultiMod-AI-Agent/
├── app/
│ ├── main.py # Streamlit or FastAPI app
│ ├── agent.py # Multi-modal reasoning logic
│ ├── image_processor.py # Embeddings from wildfire images
│ ├── doc_parser.py # PDF/DOCX/text chunking
│ ├── vector_store.py # Store + retrieve chunks
│ └── utils.py
├── data/
│ ├── wildfire_images/ # Image dataset
│ └── sample_docs/ # Optional wildfire-related docs
├── Dockerfile
├── requirements.txt
└── README.md
```
---

## ✅ Example Use Cases
Identify early fire warning signs from drone imagery

Suggest containment methods based on visual context

Cross-check document guidance with actual scenarios

Use embeddings for semantic search on fire scenes

## ⚙️ How It Works

1. **Upload** image(s) and document(s)
2. Image → Caption & embed via BLIP/CLIP  
   Document → Extracted, chunked, and embedded
3. Both sets go into a vector DB
4. RAG-based agent retrieves top chunks and calls LLM to generate a response
5. Build and Run - 
```yaml
docker build -t multimod-ai-agent .
docker run -p 8000:8000 multimod-ai-agent
```
---

## 📌 Roadmap
 Vision + text fusion via RAG

 Add mic-input and audio queries

 Deploy via Hugging Face Spaces or Streamlit Cloud

 Train custom wildfire captioning model
 

## 📦 Installation

```bash
git clone https://github.com/sukanyasaha007/MultiMod-AI-Agent.git
cd MultiMod-AI-Agent
pip install -r requirements.txt
python app/main.py
```

## 🛠️ Features

🖼️ Visual grounding via CLIP/BLIP

📄 Rich doc understanding (PDFs, DOCX)

🧠 RAG + LLM for deep query responses

📤 Chat-like UX (via Streamlit or FastAPI)

🔍 Search & reasoning across modalities

## 📌 Roadmap
 Multi-modal embedding & chunking

 RAG-based agent pipeline

 Audio-based querying (mic input)

 LangGraph for multi-step reasoning

 HuggingFace Space deployment

## 🤝 Contributing
Pull requests and feature suggestions are welcome!
Let’s build the future of multi-modal AI together 💬🔗

## 📬 Contact
Sukanya Saha
🌐 LinkedIn
💻 GitHub

