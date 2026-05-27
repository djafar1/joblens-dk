from joblens.parsing.text_cleaner import (
    clean_text,
    normalize_control_characters,
    normalize_unicode,
    normalize_whitespace,
)


# -------------------------
# normalize_whitespace tests
# -------------------------

def test_normalize_whitespace_strips_outer_whitespace():
    text = "   Python and Docker   "

    result = normalize_whitespace(text)

    assert result == "Python and Docker"


def test_normalize_whitespace_collapses_multiple_spaces_inside_paragraph():
    text = "Python     Docker      SQL"

    result = normalize_whitespace(text)

    assert result == "Python Docker SQL"


def test_normalize_whitespace_converts_single_newlines_inside_paragraph_to_spaces():
    text = "Python\nDocker\nSQL"

    result = normalize_whitespace(text)

    assert result == "Python Docker SQL"


def test_normalize_whitespace_preserves_paragraph_breaks():
    text = "Python     Docker\n\nSQL   PostgreSQL"

    result = normalize_whitespace(text)

    assert result == "Python Docker\n\nSQL PostgreSQL"


def test_normalize_whitespace_collapses_multiple_blank_lines_to_single_paragraph_break():
    text = "Python\n\n\n\nDocker"

    result = normalize_whitespace(text)

    assert result == "Python\n\nDocker"


def test_normalize_whitespace_handles_blank_lines_with_spaces():
    text = "Python\n   \nDocker"

    result = normalize_whitespace(text)

    assert result == "Python\n\nDocker"


def test_normalize_whitespace_removes_empty_paragraphs():
    text = "   \n\n   \n\n  Python  \n\n   Docker   \n\n"

    result = normalize_whitespace(text)

    assert result == "Python\n\nDocker"


def test_normalize_whitespace_empty_string_returns_empty_string():
    text = ""

    result = normalize_whitespace(text)

    assert result == ""


def test_normalize_whitespace_only_whitespace_returns_empty_string():
    text = "   \n\t   \n   "

    result = normalize_whitespace(text)

    assert result == ""


# -----------------------
# normalize_unicode tests
# -----------------------

def test_normalize_unicode_composes_combining_accent():
    text = "Cafe\u0301"

    result = normalize_unicode(text)

    assert result == "Café"


def test_normalize_unicode_preserves_danish_characters():
    text = "læring søgning prædiktion"

    result = normalize_unicode(text)

    assert result == "læring søgning prædiktion"


def test_normalize_unicode_preserves_accented_words():
    text = "Café naïve résumé"

    result = normalize_unicode(text)

    assert result == "Café naïve résumé"


def test_normalize_unicode_preserves_technical_terms():
    text = "C++ C# .NET CI/CD Node.js Python"

    result = normalize_unicode(text)

    assert result == "C++ C# .NET CI/CD Node.js Python"


# ----------------------------------
# normalize_control_characters tests
# ----------------------------------

def test_normalize_control_characters_converts_windows_line_endings_to_newline():
    text = "Python\r\nDocker"

    result = normalize_control_characters(text)

    assert result == "Python\nDocker"


def test_normalize_control_characters_converts_old_mac_line_endings_to_newline():
    text = "Python\rDocker"

    result = normalize_control_characters(text)

    assert result == "Python\nDocker"


def test_normalize_control_characters_converts_tabs_to_spaces():
    text = "Python\tDocker\tSQL"

    result = normalize_control_characters(text)

    assert result == "Python Docker SQL"


def test_normalize_control_characters_preserves_newlines():
    text = "Python\nDocker\nSQL"

    result = normalize_control_characters(text)

    assert result == "Python\nDocker\nSQL"


def test_normalize_control_characters_removes_zero_width_space():
    text = "Py\u200bthon"

    result = normalize_control_characters(text)

    assert result == "Python"


def test_normalize_control_characters_removes_null_character():
    text = "Python\x00Docker"

    result = normalize_control_characters(text)

    assert result == "PythonDocker"


def test_normalize_control_characters_preserves_technical_terms():
    text = "C++ C# .NET CI/CD Node.js"

    result = normalize_control_characters(text)

    assert result == "C++ C# .NET CI/CD Node.js"


# ----------------
# clean_text tests
# ----------------

def test_clean_text_runs_full_pipeline():
    text = "  Cafe\u0301\tPython\r\n\r\nDocker     CI/CD  "

    result = clean_text(text)

    assert result == "Café Python\n\nDocker CI/CD"


def test_clean_text_preserves_paragraphs():
    text = "  Experience with Python\n\nWorked with Docker and SQL  "

    result = clean_text(text)

    assert result == "Experience with Python\n\nWorked with Docker and SQL"


def test_clean_text_preserves_technical_terms():
    text = "  Experience with C++, C#, .NET, CI/CD, Node.js and Python  "

    result = clean_text(text)

    assert result == "Experience with C++, C#, .NET, CI/CD, Node.js and Python"


def test_clean_text_handles_pdf_like_spacing():
    text = "  Machine   Learning\n\n\nNatural     Language\tProcessing\r\nDocker  "

    result = clean_text(text)

    assert result == "Machine Learning\n\nNatural Language Processing Docker"


def test_clean_text_removes_invisible_characters_but_keeps_words_readable():
    text = "Py\u200bthon and Dock\u200ber"

    result = clean_text(text)

    assert result == "Python and Docker"


def test_clean_text_empty_string_returns_empty_string():
    text = ""

    result = clean_text(text)

    assert result == ""


def test_clean_text_only_whitespace_returns_empty_string():
    text = "   \n\n\t   "

    result = clean_text(text)

    assert result == ""


def test_clean_text_preserves_danish_text():
    text = "  Jeg har erfaring med maskinlæring, søgning og prædiktion.  "

    result = clean_text(text)

    assert result == "Jeg har erfaring med maskinlæring, søgning og prædiktion."