# 🤖 MultiMod-AI-Agent

A cutting-edge multi-modal agent that understands and reasons over **both images and documents** using vision models and LLMs. Ask natural language questions, and get smart, grounded answers combining document content and visual context. Built with ❤️ for AI + Agentic workflows.

---

## 🚀 Demo Use Cases

> Upload an image of a chip layout + a design document  
> Ask: **"Does this image align with the constraints in section 2 of the spec?"**

> Upload a flowchart + system architecture PDF  
> Ask: **"What’s the main difference in the data pipeline between these two?"**

---

## 🧠 Tech Stack

| Component        | Tech                                                  |
|------------------|-------------------------------------------------------|
| **Vision Models** | BLIP / CLIP (`transformers`, `sentence-transformers`) |
| **Document Parsing** | `PyMuPDF`, `unstructured`, `docx2txt`               |
| **Vector Store** | PGVector / Chroma / FAISS                            |
| **LLM Interface** | LLaMA3 via Ollama / GPT-4 via LangChain              |
| **Agent Engine** | `LangChain` multi-modal agents                        |
| **App Layer**    | FastAPI or Streamlit for chat + file upload UI       |

---

## 📂 Project Structure

