from transformers import pipeline

def initialize_model():
    """
    Inicializa o modelo XLM-RoBERTa para análise de preenchimento de máscaras.
    """
    print("Inicializando o modelo XLM-RoBERTa...")
    return pipeline("fill-mask", model="xlm-roberta-base")

def correct_and_suggest(pipe):
    """
    Recebe uma frase do usuário, aplica correção e sugere melhorias para fluidez.
    """
    sentence = input("Digite uma frase para correção: ")
    
    
    if not sentence.strip():
        print("A frase está vazia. Tente novamente.")
        return

    words = sentence.split()
    suggestions = []

    print("\nProcessando... Por favor, aguarde.\n")

    for i, word in enumerate(words):
        masked_sentence = " ".join(words[:i] + ["<mask>"] + words[i+1:])
        results = pipe(masked_sentence)

        
        best_suggestion = results[0]['token_str']
        explanation = f"Substituímos '{words[i]}' por '{best_suggestion}' para melhorar a fluidez."
        suggestions.append((words[i], best_suggestion, explanation))

    print("\n-- Sugestões de Correção e Fluidez ---")
    for original, suggestion, explanation in suggestions:
        print(f"- Original: {original}")
        print(f"  Sugestão: {suggestion}")
        print(f"  Explicação: {explanation}\n")

if __name__ == "__main__":
    pipe = initialize_model()
    correct_and_suggest(pipe)
