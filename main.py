import os

LINE = "The soap dish holds the soap, drains the water, and is somehow the dirtiest thing in the bathroom."

# Mirror of the bounty gate in RULES.txt: /output/entry.txt must be
# UTF-8 text of 1 to 200 characters, not only white space, one line.
def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if len(text) < 1 or len(text) > 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text

def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
