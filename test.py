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

def process_input(gf, tool, input_text, option):
    sentences = split_sentences(input_text)
    corrected_sentences = []
    all_explanations = []

    for part in sentences:
        corrected_part = correct(gf, part)
        explanations = explain(tool, corrected_part)

        corrected_sentences.append(corrected_part)
        all_explanations.extend(explanations)

    corrected_text = " ".join(corrected_sentences)

    result = ""
    if option == "1":
        result = f"Correção do Gramformer:\n- Corrigido: {corrected_text}"
    elif option == "2":
        result = "Explicações do LanguageTool:\n"
        if all_explanations:
            for explanation in all_explanations:
                result += f"- Erro: {explanation['error']}\n  Sugestão: {', '.join(explanation['suggestion'])}\n  Motivo: {explanation['message']}\n"
        else:
            result += "Nenhum erro encontrado ou explicações disponíveis."
    elif option == "3":
        result = f"Correção do Gramformer:\n- Corrigido: {corrected_text}\n\nExplicações do LanguageTool:\n"
        if all_explanations:
            for explanation in all_explanations:
                result += f"- Erro: {explanation['error']}\n  Sugestão: {', '.join(explanation['suggestion'])}\n  Motivo: {explanation['message']}\n"
        else:
            result += "Nenhum erro encontrado ou explicações disponíveis."
    else:
        result = "Opção inválida. Por favor, escolha uma das opções fornecidas."

    return result

def main():
    print("Inicializando modelos, aguarde...")
    gf = initialize_gramformer()
    tool = initialize_languagetool()

    print("Bem-vindo ao corretor de frases!")
    print("Escolha como deseja processar suas frases:")
    print("1. Apenas correção\n2. Apenas sugestões\n3. Ambos (sugestão e correção)")

    option = input("Digite o número da sua escolha: ").strip()

    while True:
        print("\nDigite uma frase para correção (ou 'sair' para encerrar):")
        input_text = input().strip()

        if input_text.lower() == 'sair':
            print("Encerrando o programa. Até logo!")
            break

        result = process_input(gf, tool, input_text, option)
        print(f"\n{result}\n")

if __name__ == "__main__":
    main()
