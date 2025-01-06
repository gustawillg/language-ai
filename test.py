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
    jfleg = load_dataset("jhu-clsp/jfleg", split='validation')  # Carrega o dataset JFLEG
    jfleg_df = pd.DataFrame(jfleg)  # Converte o dataset JFLEG para DataFrame

    print("Colunas do jfleg_df:", jfleg_df.columns)
    
    combined_df = jfleg_df[['sentence']]  # Apenas utiliza a coluna 'sentence' do JFLEG
    print(f"Total de exemplos combinados: {len(combined_df)}")
    return combined_df 

def main():
    gf = initialize_gramformer()
    combined_dataset = load_datasets()
    
    while True:
        sentence = input("\nDigite uma frase para correção (ou 'sair' para encerrar): ").strip()
        if sentence.lower() == "sair":
            print("Encerrando o programa. Até mais!")
            break

        corrected = correct_sentence(gf, sentence)  # Correção da frase do usuário
        print("\n-- Sugestões de Correção e Fluidez ---")
        print(f"- Original: {sentence}")
        print(f"- Sugestão: {corrected}")

if __name__ == "__main__":
    main()
