def main():
    print("--- DecodeLabs Logic Engine v1.0 [Verified] ---")
    print("System: Online. Logic Skeleton: Active.")
    print("(Type 'exit' to terminate the session)\n")


    responses = {
        "hello":      "Greetings! I am your deterministic logic engine.",
        "hi":         "Greetings! I am your deterministic logic engine.",
        "hey":        "Greetings! I am your deterministic logic engine.",
        "project 1":  "Project 1 focuses on Control Flow and Logic using a White Box approach.",
        "white box":  "A White Box ensures traceability and zero hallucination risk.",
        "decodelabs": "DecodeLabs: Training the next generation of AI Engineers.",
        "ipo model":  "The IPO Model: Input (Sanitization) → Process (Logic) → Output (Feedback).",
        "guardrails": "AI Guardrails are deterministic filters that wrap probabilistic LLM outputs.",
        "hybrid":     "Hybrid Architecture: Rule match → Instant response; No match → Pass to LLM.",
    }


    while True:


        try:
            raw_input_text = input("USER INPUT > ")
        except EOFError:
            break


        clean_input = raw_input_text.lower().strip()


        if clean_input in ('exit', 'quit', 'terminate'):
            print("Chatbot: [Process Complete] Terminating loop. Goodbye.")
            break


        response = responses.get(clean_input, "Input unrecognized. Please provide a predefined command.")
        print(f"CHATBOT RESPONSE > {response}\n")


if __name__ == "__main__":
    main()