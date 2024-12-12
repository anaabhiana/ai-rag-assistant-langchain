from langchain.text_splitter import RecursiveCharacterTextSplitter

# Define the LaTeX text
latex_text = """
    \documentclass{article}

    \begin{document}

    \maketitle

    \section{Introduction}

    Large language models (LLMs) are a type of machine learning model that can be trained on vast amounts of text data to generate human-like language. In recent years, LLMs have made significant advances in various natural language processing tasks, including language translation, text generation, and sentiment analysis.

    \subsection{History of LLMs}

    The earliest LLMs were developed in the 1980s and 1990s, but they were limited by the amount of data that could be processed and the computational power available at the time. In the past decade, however, advances in hardware and software have made it possible to train LLMs on massive datasets, leading to significant improvements in performance.

    \subsection{Applications of LLMs}

    LLMs have many applications in the industry, including chatbots, content creation, and virtual assistants. They can also be used in academia for research in linguistics, psychology, and computational linguistics.

    \end{document}
"""

# Initialize the text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,  # Maximum size of each chunk
    chunk_overlap=50,  # Overlap between chunks for context retention
)

# Split the LaTeX text into chunks
chunks = splitter.split_text(latex_text)

# Display the results
print("Number of chunks:", len(chunks))
print("Chunks:")
for idx, chunk in enumerate(chunks, 1):
    print(f"\nChunk {idx}:\n{chunk}")