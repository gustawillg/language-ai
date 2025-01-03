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
    
    
    masked_sentence = sentence + "<mask>"

    print("\nProcessando... Por favor, aguarde.\n")

    results = pipe(masked_sentence)
    best_suggetion = results[0]['results']

    print("\n-- Sugestões de Correção e Fluidez ---")
    print(f"- Original: {sentence}")
    print(f"  Sugestão: {best_suggetion}")
    print(f"Explicação: O modelo ajustou a frase considerando a fluidez e gramática.\n")

if __name__ == "__main__":
    pipe = initialize_model()
    correct_and_suggest(pipe)
