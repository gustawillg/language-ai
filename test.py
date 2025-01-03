from transformers import T5Tokenizer, T5ForConditionalGeneration

def initialize_model():
    print("Inicializando o modelo T5 para correção gramatical...")
    model = T5ForConditionalGeneration.from_pretrained("t5-small")
    tokenizer = T5Tokenizer.from_pretrained("t5-small")
    return model, tokenizer

def correct_sentence(model, tokenizer):
    sentence = input("Digite uma frase para correção: ")

    print("\nProcessando... Por favor, aguarde.\n")

    input_text = f"grammar correction: {sentence}"
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    outputs = model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
    corrected_sentence = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("\n-- Sugestões de Correção e Fluidez ---")
    print(f"- Original: {sentence}")
    print(f"- Sugestão: {corrected_sentence}")

if __name__ == "__main__":
    model, tokenizer = initialize_model()
    correct_sentence(model, tokenizer)
