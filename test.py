from datasets import load_dataset
from gramformer import Gramformer
import pandas as pd


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

def load_datasets():
    jfleg = load_dataset("jhu-clsp/jfleg", split='train')

    clang8_path = "./datasets/clang8.csv"
    clang8 = pd.read_csv(clang8_path)

    jfleg_df = pd.DataFrame(jfleg)
    combined_df = pd.concat([jfleg_df[['sentence', 'corrected']], clang8[['source', 'target']]], ignore_index=True)

    print(f"Total de exemplos combinados: {len(combined_df)}")
    return combined_df 

def fine_tune(gf, dataset):
    for i, row in dataset.iterrows():
        original_sentence = row['source']
        corrected_sentence = row['target']          
        corrections = gf.correct(original_sentence, max_candidates=1)
        print(f"Original: {original_sentence}")
        print(f"Correção sugerida: {corrections[0]}")

def main():
    gf = initialize_gramformer()

    combined_dataset = load_datasets()

    fine_tune(gf, combined_dataset)

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
