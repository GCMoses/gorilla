import openai
import streamlit as st
import subprocess
openai.api_key = "EMPTY" # Key is ignored and does not matter
openai.api_base = "http://zanino.millennium.berkeley.edu:8000/v1"
#Query Gorilla Server
def get_gorilla_response(prompt, model):
    try:
        completion = openai.ChatCompletion.create(
            model = model,
            messages = [{"role": "user", "content": prompt}]
        )
        print("Response: ", completion)
        return completion.choices[0].message.content 
    except Exception as e:
        print("Sorry, something went wrong!")
def extract_code_from_output(output):
    code =output.split("code>>>:")[1]
    return code
def run_generated_code(file_path):
    # Command to run the generated code using Python interpreter
    command = ["python", file_path]
    try:
        # Execute the command as a subprocess and capture the output and error streams
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Check if the subprocess ran successfully
        if result.returncode == 0:
            st.success("Generated code executed successfully.")
            # Display the output of the generated code
            st.code(result.stdout, language="python")
        else:
            st.error("Generated code execution failed with the following error:")
            # Display the error message
            st.code(result.stderr, language="bash")
    
    except Exception as e:
        st.error("Error occurred while running the generated code:", e)
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    .stTextInput {
        background-color: #f5f5f5;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        padding: 8px;
        color: #333333; 
        background: url('gorilla.png') no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("Dev Solution AI Gorilla")
    
    custom_css = '''
    <style>
        div.css-1om1ktf.e1y61itm0 {
            content: "";
            position: absolute;
            inset: -4px -5px;
            z-index: -1;
            background: linear-gradient(to right, rgb(237, 110, 97), rgb(99, 89, 225));
            border-radius: 18px;
        }
    </style>
    '''
    st.markdown(custom_css, unsafe_allow_html=True)
    
    input_prompt = st.text_area(
        "Enter your prompt below:",
        key="text_input",
        height=100
    )
    option = st.selectbox('Select a model option from the list:', ('gorilla-7b-hf-v1', "gorilla-mpt-7b-hf-v0"))
    if st.button("King Kong Huntin"):
        if len(input_prompt) > 0:
            col1, col2 = st.columns([1,1])
            with col1:
                if option == "gorilla-7b-hf-v1":
                    result = get_gorilla_response(prompt=input_prompt, model=option)
                    st.write(result)
                elif option == "gorilla-mpt-7b-hf-v0":
                    result = get_gorilla_response(prompt=input_prompt, model=option)
                    st.write(result)
            with col2:
                # pass
                if option == "gorilla-7b-hf-v1":
                    code_result = extract_code_from_output(result)
                    st.subheader("Generated Output")
                    st.code(code_result, language='python')
                elif option == "gorilla-mpt-7b-hf-v0":
                    code_result = extract_code_from_output(result)  
                    lines = code_result.split('\\n')
                    for i in range(len(lines)-1):
                        st.code(lines[i], language='python')
                    
if __name__ == "__main__":
    main()