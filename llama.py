from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import time
import PyPDF2
import random
from fpdf import FPDF

# Initialize the Ollama model with the specified model name
llm = Ollama(model="llama3")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_filename):
    with open(pdf_filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Define a prompt template for generating MCQs
prompt_template = PromptTemplate(
    input_variables=["content", "num_questions"],
    template="""Based on the following content, generate {num_questions} multiple-choice questions. 
    For each question, provide 4 options (A, B, C, D) and indicate the correct answer.
    Format:
    Q1. [Question]
    A. [Option A]
    B. [Option B]
    C. [Option C]
    D. [Option D]
    Correct Answer: [A/B/C/D]
    Q2. ...

    Content:
    {content}
    """
)

# Create a chain using the prompt template and the Ollama model
mcq_chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

# Function to generate MCQs from PDF content and save to a new PDF
def generate_mcqs_from_pdf(input_pdf, output_pdf, num_questions):
    content = extract_text_from_pdf(input_pdf)
    start_time = time.time()
    response = mcq_chain.run(content=content, num_questions=num_questions)
    end_time = time.time()
    
    # Create new PDF with generated MCQs
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, response)
    pdf.output(output_pdf)
    
    execution_time = end_time - start_time
    print(f"MCQs generated based on {input_pdf} and saved to {output_pdf}")
    print(f"Execution time: {execution_time:.2f} seconds")

# Function to create a quiz from the MCQ PDF
def create_quiz_from_pdf(pdf_filename):
    with open(pdf_filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    
    questions = text.split('Q')[1:]  # Split by 'Q' to separate questions
    random.shuffle(questions)  # Randomize question order
    
    for i, question in enumerate(questions, 1):
        print(f"Q{i}.{question.split('Correct Answer:')[0]}")
        input("Press Enter to see the correct answer...")
        print(f"Correct Answer:{question.split('Correct Answer:')[1].strip()}\n")

# Example usage
num_questions = 5
input_pdf = "/home/natty/llama/comnets-1st-prelim-handouts.pdf"
output_pdf = "/home/natty/llama/generated_mcqs.pdf"

# Generate MCQs from input PDF and save to output PDF
generate_mcqs_from_pdf(input_pdf, output_pdf, num_questions)

# Create a quiz from the generated MCQ PDF
print("\nLet's start the quiz!")
create_quiz_from_pdf(output_pdf)