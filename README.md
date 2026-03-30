# 🚀 LangChain Memory Practice

This repository demonstrates different memory techniques in LangChain to build context-aware AI applications.

## 📌 What is Memory in LangChain?
Memory allows AI models to remember previous interactions and use that context in future responses. Without memory, each query is treated independently.

## 🔍 Implemented Memory Types

### 1. ConversationBufferMemory
- Stores full conversation history
- Best for short chats

### 2. ConversationBufferWindowMemory
- Stores only last k interactions
- Helps reduce token usage

### 3. ConversationSummaryMemory
- Summarizes long conversations
- Best for long chats

## 🛠 Tech Stack
- Python
- LangChain
- OpenAI

## ▶️ How to Run

pip install langchain openai  
python buffer_memory.py  

## 📊 Example Output

Hi, my name is Taha Ahmad  
Your name is Taha Ahmad  

## 💡 Key Learnings
- Memory helps AI remember context
- Different memory types serve different use cases
- Summary memory improves performance in long chats

## 🎯 Conclusion
Understanding memory in LangChain is important for building smart AI chatbots and assistants.
