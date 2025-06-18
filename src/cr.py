import openai
import os

# Set OpenAI API key

#openai.api_key =  os.environ["op://AWS_training/OpenAPICred/credential"]
# Access secret value from secret key reference using 1Password CLI tool
def get_secret_value():
    return os.popen(f'op read "op://AWS_training/OpenAPICred/credential"').read().strip()

# Retrieve the secret value by providing the secret key reference
openai.api_key = get_secret_value()

# Function to analyze code with OpenAI
def analyze_code(code):
    code="perform thrat modelling on below and and provide risks analysis wigth vulnerbailities"+code
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=code,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1
    )
    return response.choices[0].text.strip()

# Function to read code files from a folder and analyze them
def analyze_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".php"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                code = file.read()
                print(f"Analyzing code in file: {file_name}")
                suggestions = analyze_code(code)
                print(f"Suggestions for {file_name}:")
                print(suggestions)

# Provide the folder path containing code files
folder_path = "C:/Users/psmkr/Downloads/phpvulnbank-master/phpvulnbank-master/src/"

# Call the function to analyze the folder
analyze_folder(folder_path)
