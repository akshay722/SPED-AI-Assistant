from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=50,
        length_function=len
    )
    return text_splitter.split_text(text)