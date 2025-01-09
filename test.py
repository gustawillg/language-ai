from gramformer import Gramformer
import language_tool_python
import re

def initialize_gramformer():
    return Gramformer(models=1)

def initialize_languagetool():
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
            break

        option = input("Escolha uma opção: (1) Apenas correção, (2) Apenas sugestões, (3) Ambos: ").strip()
        sentences = split_sentences(sentence)
        corrected_sentences = []
        all_explanations = []

        for part in sentences:
            corrected_part = correct(gf, part) if option in ["1", "3"] else part
            explanations = explain(tool, corrected_part) if option in ["2", "3"] else []
            corrected_sentences.append(corrected_part)
            all_explanations.extend(explanations)

        corrected_text = " ".join(corrected_sentences)

        if option in ["1", "3"]:
            print("\nCorreção do Gramformer:")
            print(f"- Original: {sentence}")
            print(f"- Corrigido: {corrected_text}")

        if option in ["2", "3"]:
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
