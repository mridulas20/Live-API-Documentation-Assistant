import pathway as pw
from llm_agent import answer_with_llm

# Live-read markdown docs
docs = pw.io.fs.read(
    "./api_docs",
    format="plaintext",
    with_metadata=True
)

def main():
    print(" API Doc Assistant ready. Ask a question.\n")

    while True:
        query = input(">> ").strip()
        if not query:
            continue

        rows = docs.to_pandas()["data"].tolist()
        context = "\n".join(rows)

        answer = answer_with_llm(query, context)
        print("\nANSWER:\n", answer, "\n")

pw.run(main)
