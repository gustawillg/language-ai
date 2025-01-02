from transformers import pipeline

def initialize_mode():
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
    words = sentence.split()
    suggestions = []

    print("\nProcessando... Por favor, aguarde. \n")

    for i in range(len(words)):
        masked_setence= " ".join(words[:i] + ["<mask>"] + words[i+1:])
        results = pipe(masked_setence)

        best_suggestion = results[0]['sequence']
        explanation = f"Substituímos '{words[i]}' por '{best_suggestion.split()[i]}' para melhorar a fluidez."
        suggestions.append((words[i], best_suggestion, explanation))

    print("\n-- Sugestões de Correção e Fluidez ---")
    for original, suggestion, explanation in suggestions:
        print(f"- Original: {original}")
        print(f" Sugestão: {suggestion}")
        print(f" Explicação: {explanation}\n")

if __name__ == "__main__":
    pipe = initialize_mode()
    correct_and_suggest(pipe)