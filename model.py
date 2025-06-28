import google.generativeai as genai

# Configure Gemini API key
gemini_api_key = "AIzaSyDEP54Uf0_VqHlzzQcWJ0TpdUtnkzgJMos"
genai.configure(api_key=gemini_api_key)

# Load the Gemini model
model = genai.GenerativeModel("models/gemini-2.0-flash-001")

# Define the function to run different prompt types
def run_prompt(prompt_type, user_input):
    if prompt_type == "Zero-Shot":
        prompt = f"{user_input}"

    elif prompt_type == "Few-Shot":
        prompt ={
            "Q : who is the President of INDIA \n\n"
            "A : Ms.Draupadi Murmu"
            "Q : who is the President of United State \n\n"
            "A : Mr.Donald Trump"
            f"Q{user_input}\n"
            "A : "
        }
    
    elif prompt_type =="Instruction-Based":
        prompt =(
            "Istruction : Summarize my article in 3 bullet points"
            f"Text : {user_input}"
        )
    
    elif prompt_type == "Chain-of-Thought":
        prompt = (
            "Solve the following neural network backpropagation equation step-by-step:\n"
            f"Problem: {user_input}\n"
            "Solution:"
        )

    elif prompt_type == "Role-based":
        prompt = (
            "You are a real estate consultant. Please explain where and why someone should purchase property in Gurgaon."
        )

    else:
        prompt = user_input

    # Generate content using Gemini
    response = model.generate_content(prompt)
    return response.text.strip()