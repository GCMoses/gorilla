# gorilla
<div style="background-image: url('gorilla.png'); background-repeat: no-repeat; background-size: cover;">

Create a new directory for your project and navigate to that directory in your command prompt or terminal.
Create a new virtual environment for your project by running the following command:
python -m venv myenv
Activate the virtual environment. The command to activate the virtual environment depends on your operating system:
For Windows:
     myenv\Scripts\activate
     ```
For macOS/Linux:
     source myenv/bin/activate
     ```
Create a new file called requirements.txt in the project directory and add the following dependencies to it:
transformers
diffusers
torch
pandas
numpy

Install the required dependencies by running the following command:

pip install -r requirements.txt

Save the provided code in a file called app.py in the project directory.

Save the app.py file.

In your command prompt or terminal, run the following command to start the Streamlit app:

streamlit run app.py

The Streamlit app will start running, and you can access it in your web browser at http://localhost:8501.

You can enter your prompt in the text area provided and select a model option from the dropdown list.

Click the "King Kong Huntin" button to generate a response based on your prompt using Gorilla LLM.

The generated response will be displayed in the app. If the response includes generated code, it will be shown in a separate section.

To run the generated code, copy the code and paste it into a .py file  The generated code will be executed, when you run streamlit run newwly-generated.py to see the results of Goorilla LLM
</div>
