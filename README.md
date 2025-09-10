#!/bin/bash
# ==========================================================
# 📘 PDF to MCQ Generator
# ==========================================================
# This project:
#   1. Extracts text from a PDF
#   2. Uses Ollama (LLaMA 3) + LangChain to generate MCQs
#   3. Saves MCQs into a new PDF
#   4. Runs an interactive quiz in the terminal
# ==========================================================

# ----------------------------------------------------------
# 🚀 Features
# ----------------------------------------------------------
# 📄 Extracts text from any PDF
# 🤖 Generates MCQs with LangChain + Ollama (LLaMA 3)
# 📝 Saves MCQs into a PDF
# 🎲 Shuffles questions for quiz sessions
# 🎮 Interactive quiz mode in terminal
# ----------------------------------------------------------

# ----------------------------------------------------------
# 📂 Project Structure
# ----------------------------------------------------------
# .
# ├── main.py
# ├── comnets-1st-prelim-handouts.pdf   # Example input
# ├── generated_mcqs.pdf                # Output with MCQs
# └── README.md
# ----------------------------------------------------------

# ----------------------------------------------------------
# 🛠️ Requirements
# ----------------------------------------------------------
pip install langchain-community langchain PyPDF2 fpdf

# Install Ollama: https://ollama.ai/download
ollama pull llama3
# ----------------------------------------------------------

# ----------------------------------------------------------
# ▶️ Usage
# ----------------------------------------------------------

# 1. Edit `main.py`:
# ----------------------------------------------------------
# input_pdf = "/path/to/your/input.pdf"
# output_pdf = "/path/to/your/output.pdf"
# num_questions = 5
# ----------------------------------------------------------

# 2. Run the script:
python main.py

# Actions performed:
#   - Extract text from input.pdf
#   - Generate N MCQs
#   - Save them into output.pdf
#   - Start quiz mode
# ----------------------------------------------------------

# ----------------------------------------------------------
# 🎮 Quiz Mode
# ----------------------------------------------------------
# - Questions shown one by one (random order)
# - Press ENTER to reveal answer
# ----------------------------------------------------------

# ----------------------------------------------------------
# 📖 Example Output
# ----------------------------------------------------------
# Q1. What does TCP stand for?
# A. Transmission Control Protocol
# B. Transfer Communication Protocol
# C. Transport Communication Process
# D. Transmission Connect Process
# Correct Answer: A
# ----------------------------------------------------------

# ----------------------------------------------------------
# ✨ Future Improvements
# ----------------------------------------------------------
# - GUI for easier quiz taking
# - Export quiz results (score report)
# - OCR support for scanned PDFs
# ----------------------------------------------------------
