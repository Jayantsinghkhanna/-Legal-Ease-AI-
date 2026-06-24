import re


SECTION_PATTERN = r"\n\d+\.\s+[A-Z][^\n]+"


def extract_sections(text):

    matches = list(
        re.finditer(
            SECTION_PATTERN,
            text
        )
    )

    sections = []

    for i in range(len(matches)):

        start = matches[i].start()

        end = (
            matches[i + 1].start()
            if i + 1 < len(matches)
            else len(text)
        )

        chunk = text[start:end]

        title = matches[i].group().strip()

        sections.append(
            {
                "section": title,
                "content": chunk
            }
        )

    return sections