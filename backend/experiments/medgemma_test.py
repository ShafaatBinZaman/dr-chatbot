import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def test_medgemma():
    model_id = "google/medgemma-4b-it"  # instruction-tuned version
    # or use "google/medgemma-4b-pt" for pre-trained version

    print("Loading tokenizer and model:", model_id)
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto"  # if you have GPU; else device_map="cpu"
    )

    pipe = pipeline(
        "text-generation",  # or "text2text-generation" depending on your prompt style
        model=model,
        tokenizer=tokenizer,
        device=0 if torch.cuda.is_available() else -1
    )

    user_input = "I have a persistent headache and vision disturbance. What could this be?"
    print("User input:", user_input)

    result = pipe(
        user_input,
        max_new_tokens=150,
        temperature=0.7,
        repetition_penalty=2.0,
        top_p=0.9
    )

    print("Model output:", result[0]["generated_text"])

if __name__ == "__main__":
    test_medgemma()
