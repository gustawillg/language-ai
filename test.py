from gramformer import Gramformer
import language_tool_python
import re

def initialize_gramformer():
    print("Inicializando Gramformer...")
    return Gramformer(models=1)

def initialize_languagetool():
    print("Inicializando LanguageTool...")
    return language_tool_python.LanguageTool('en-US')

def split_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)

def correct(gf, sentence):
    corrections = list(gf.correct(sentence, max_candidates=1))
    return corrections[0] if corrections else sentence

def explain(tool, corrected_sentence):
    matches = tool.check(corrected_sentence)
    explanations = []
    for match in matches:
        explanations.append({
            "error": match.context,
            "suggestion": match.replacements,
            "message": match.message
        })
    return explanations

def main():
    gf = initialize_gramformer()
    tool = initialize_languagetool()

    while True:
        sentence = input("Digite uma frase para correção (ou 'sair' para encerrar): ").strip()
        if sentence.lower() == "sair":
            print("Encerrando o programa.")
            break

        sentences = split_sentences(sentence)
        corrected_sentences = []
        all_explanations = []

        for part in sentences:
            corrected_part = correct(gf, part)
            explanations = explain(tool, corrected_part)
            corrected_sentences.append(corrected_part)
            all_explanations.extend(explanations)

        corrected_text = " ".join(corrected_sentences)

        print("\nCorreção do Gramformer:")
        print(f"- Original: {sentence}")
        print(f"- Corrigido: {corrected_text}")
        print("\nExplicações do LanguageTool:")
        if all_explanations:
            for explanation in all_explanations:
                print(f"- Erro: {explanation['error']}")
                print(f"  Sugestão: {', '.join(explanation['suggestion'])}")
                print(f"  Motivo: {explanation['message']}")
        else:
            print("Nenhum erro encontrado ou explicações disponíveis.")

if __name__ == "__main__":
    main()
