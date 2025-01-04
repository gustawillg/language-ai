from gramformer import Gramformer

def initialize_gramformer():
    print("Inicializando o modelo Gramformer...")
    gf = Gramformer(models=1)
    print("Gramformer inicializado com sucesso!")
    return gf

def correct_sentence(gf, sentence):
    print("\nProcessando... Por favor, aguarde.\n")
    corrections = list(gf.correct(sentence, max_candidates=1))
    if corrections:
        return corrections[0]
    else:
        return "Nenhuma sugestão encontrada. A frase pode já estar correta."

def main():
    gf = initialize_gramformer()

    while True:
        sentence = input("\nDigite uma frase para correção (ou 'sair' para encerrar): ").strip()
        if sentence.lower() == "sair":
            print("Encerrando o programa. Até mais!")
            break

        corrected = correct_sentence(gf, sentence)
        print("\n-- Sugestões de Correção e Fluidez ---")
        print(f"- Original: {sentence}")
        print(f"- Sugestão: {corrected}")

if __name__ == "__main__":
    main()
