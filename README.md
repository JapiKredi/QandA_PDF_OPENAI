# chatWithPDF

This project allows you to upload a PDF document and ask questions about its content. It uses langchain, openapi ai model and Facebook Ai Similarity Search(FAISS) library to process the text in the PDF and provide answers to questions pertaining the document.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/JapiKredi/QandA_PDF_OPENAI.git

   cd into your directory/ open with vscode
   ```

2. Create a Virtual Environment:
   I am using Python 3.8

   ```shell
   python3.8 -m venv pdf
   source pdf/bin/activate
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Create OpenAI API Key and add it to your .env file:
   [openai](https://platform.openai.com/)
   ```shell
   Specify the variable as follows :
   OPENAI_API_KEY = "Secret Key"
   ```
5. Run the application:

   ```shell
   streamlit run app.py
   ```

## Next Steps

1. Add support for multiple file formats
2. Implement Document Indexing techniques by use of libraries such as Elasticsearch or Apache Solr
3. Enhance question answering capabilities: Explore advanced question answering techniques, such as using transformer models like BERT or GPT, to improve the accuracy and comprehension of the system.
4. Use a model that supports multiple languages, most notably some BERT models do support this.
