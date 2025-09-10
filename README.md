# 📘 PDF to MCQ Generator

An intelligent tool that extracts text from PDFs and generates multiple-choice questions using LLaMA 3 via Ollama and LangChain.

## 🚀 Features

- 📄 **PDF Text Extraction** - Extract text from any PDF document
- 🤖 **AI-Powered MCQ Generation** - Generate questions using LangChain + Ollama (LLaMA 3)
- 📝 **PDF Export** - Save generated MCQs into a formatted PDF
- 🎲 **Randomized Quizzes** - Shuffled questions for varied quiz sessions
- 🎮 **Interactive Terminal Quiz** - Take quizzes directly in your terminal

## 📂 Project Structure

```
.
├── main.py
├── comnets-1st-prelim-handouts.pdf   # Example input PDF
├── generated_mcqs.pdf                # Generated MCQs output
└── README.md
```

## 🛠️ Installation & Setup

### Install Dependencies

```bash
# Install Python packages
pip install langchain-community langchain PyPDF2 fpdf

# Install Ollama
# Visit: https://ollama.ai/download

# Pull LLaMA 3 model
ollama pull llama3
```

## ▶️ Usage

### 1. Configure Your Files

Edit the configuration in `main.py`:

```python
input_pdf = "/path/to/your/input.pdf"
output_pdf = "/path/to/your/output.pdf"
num_questions = 5
```

### 2. Run the Generator

```bash
python main.py
```

**What happens:**
1. Extracts text from your input PDF
2. Generates N multiple-choice questions
3. Saves MCQs to output PDF
4. Launches interactive quiz mode

## 🎮 Quiz Mode

- Questions displayed in random order
- Multiple choice options (A, B, C, D)
- Press **ENTER** to reveal the correct answer
- Track your progress through all questions

## 📖 Example Output

```
Q1. What does TCP stand for?
A. Transmission Control Protocol
B. Transfer Communication Protocol  
C. Transport Communication Process
D. Transmission Connect Process

Press ENTER to see answer...
Correct Answer: A
```

## 🔧 Quick Start Script

Save this as `setup.sh` for easy installation:

```bash
#!/bin/bash

echo "🚀 Setting up PDF to MCQ Generator..."

# Install Python dependencies
echo "📦 Installing Python packages..."
pip install langchain-community langchain PyPDF2 fpdf

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "⚠️  Ollama not found. Please install from https://ollama.ai/download"
    exit 1
fi

# Pull LLaMA 3 model
echo "🤖 Downloading LLaMA 3 model..."
ollama pull llama3

echo "✅ Setup complete! Run 'python main.py' to start generating MCQs."
```

Make it executable and run:

```bash
chmod +x setup.sh
./setup.sh
```

## 🎯 Usage Examples

### Basic Usage
```bash
# Generate 10 questions from a PDF
python main.py --input document.pdf --questions 10

# Specify output file
python main.py --input study-guide.pdf --output my-quiz.pdf --questions 15
```

### Batch Processing
```bash
# Process multiple PDFs
for pdf in *.pdf; do
    python main.py --input "$pdf" --questions 5
done
```

## ⚡ Requirements

- **Python 3.8+**
- **Ollama** with LLaMA 3 model
- **Internet connection** (for initial model download)
- **PDF files** for question generation

## ✨ Future Improvements

- 🖥️ **GUI Interface** - User-friendly graphical interface
- 📊 **Score Reports** - Export detailed quiz results and analytics  
- 🔍 **OCR Support** - Handle scanned PDFs and image-based documents
- 📱 **Web Interface** - Browser-based quiz taking experience
- 🎨 **Custom Themes** - Personalized quiz styling options

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
