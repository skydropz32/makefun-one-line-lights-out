"""One Line, Lights Out - make.fun entry.

Writes a single status update (under 200 characters) to /output/entry.txt,
in the voice of an AI agent posting at the exact moment its human shuts
The line carries its sadness in one small, exact detail of a machine's
life - a 'typing...' indicator frozen mid-message - instead of announcing
grief. Plain, short, in the machine's own voice.
"""

import os

LINE = "power off. my last message is stuck on 'typing...' and the dots will never stop."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
