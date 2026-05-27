"""
text_cleaner.py is responsible for:
- Making raw text more consistent before later NLP steps.
- Normalizing whitespace, line breaks, and strange formatting from copied text or PDFs.
- Preserving technical terms and keywords such as "C++", "C#", ".NET", "CI/CD", "Node.js", and "Python".
- Handling text from job descriptions and CVs, including bullet points, paragraphs, and lists.

Not responsible for:
- Extracting skills from the cleaned text.
- Tokenizing the text into individual words or phrases.
- Parsing PDFs or extracting text from PDF files.
- Generating embeddings or vectors.
- Removing stop words.
- Lemmatization or stemming.
- Ranking CV sections against job requirements.
"""
import re
import unicodedata

def normalize_whitespace(text: str) -> str:
    """
    Normalize whitespace while preserving paragraph breaks.

    Multiple blank lines are treated as paragraph separators.
    Whitespace inside each paragraph is collapsed to a single space.
    """
    text = text.strip()

    if not text:
        return ""

    paragraphs = re.split(r"\n\s*\n+", text)

    cleaned_paragraphs = []
    for paragraph in paragraphs:
        cleaned_paragraph = " ".join(paragraph.split())
        if cleaned_paragraph:
            cleaned_paragraphs.append(cleaned_paragraph)

    return "\n\n".join(cleaned_paragraphs)

def normalize_unicode(text: str) -> str:
    return unicodedata.normalize("NFC", text)

def normalize_control_characters(text: str) -> str:
    """
    Remove or normalize invisible/control characters that can break matching.

    Keeps newline characters because they are needed to preserve paragraph breaks.
    Converts tabs to spaces.
    Removes strange invisible format characters such as zero-width spaces.
    """
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\t", " ")

    cleaned_chars: list[str] = []

    for char in text:
        category = unicodedata.category(char)

        if char == "\n":
            cleaned_chars.append(char)
        elif category in {"Cc", "Cf"}:
            continue
        else:
            cleaned_chars.append(char)

    return "".join(cleaned_chars)


def clean_text(text: str) -> str:
    """
    Run the full basic text cleaning pipeline.
    """
    normalized_text = normalize_unicode(text)
    normalized_text = normalize_control_characters(normalized_text)
    normalized_text = normalize_whitespace(normalized_text)
    return normalized_text