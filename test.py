from datasets import load_dataset
from gramformer import Gramformer
import pandas as pd

def initialize_gramformer():
    gf = Gramformer(models=1)
    return gf

def correct_sentence(gf, sentence):
    corrections = list(gf.correct(sentence, max_candidates=1))
    if corrections:
        return corrections[0]
    else:
        return "Nenhuma sugestão encontrada."

def load_datasets():
    jfleg = load_dataset("jhu-clsp/jfleg", split='validation')
    jfleg_df = pd.DataFrame(jfleg)
    return jfleg_df

def fine_tune(gf, dataset):
    for i, row in dataset.iterrows():
        original_sentence = row['sentence']
        corrected_sentence = row['corrections']
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
        print(f"- Original: {sentence}")
        print(f"- Sugestão: {corrected}")

if __name__ == "__main__":
    main()
