from transformers import pipeline

def initialize_model():
    print("Inicializando o modelo XLM-RoBERTa...")
    return pipeline("fill-mask", model="xlm-roberta-base")

def correct_and_suggest(pipe):
    sentence = input("Digite uma frase para correção: ")
    words = sentence.split()
    suggestions = []

    print("\nProcessando... Por favor, aguarde.\n")

    for i in range(len(words)):
        masked_sentence = " ".join(words[:i] + ["<mask>"] + words[i+1:])
        results = pipe(masked_sentence)

        best_suggestion = results[0]['token_str']
        suggestions.append(best_suggestion)

    corrected_sentence = " ".join(suggestions)

    print("\n-- Sugestões de Correção e Fluidez ---")
    print(f"- Original: {sentence}")
    print(f"- Sugestão: {corrected_sentence}")

if __name__ == "__main__":
    pipe = initialize_model()
    correct_and_suggest(pipe)
