# -------------------------------
# 🧠 Train Your Own DrChatbot Model (No Eval Version)
# -------------------------------

from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    Trainer,
    TrainingArguments
)

# 1️⃣ Load your dataset
# Make sure dataset.csv is in the same folder with columns: "input_text","target_text"
dataset = load_dataset("csv", data_files={"train": "dataset.csv"})

# 2️⃣ Choose a lightweight base model (you can change later)
model_name = "google/flan-t5-small"

# 3️⃣ Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# 4️⃣ Preprocess data
def preprocess_function(examples):
    # Tokenize input (symptoms)
    model_inputs = tokenizer(
        examples["input_text"], 
        max_length=128, 
        truncation=True, 
        padding="max_length"   # <-- 🔥 add this line
    )
    
    # Tokenize target (advice)
    labels = tokenizer(
        examples["target_text"], 
        max_length=128, 
        truncation=True, 
        padding="max_length"   # <-- 🔥 and this too
    )
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_data = dataset.map(preprocess_function, batched=True)

# 5️⃣ Define training arguments (⚠️ eval_strategy disabled)
training_args = TrainingArguments(
    output_dir="./drchatbot-model",
    eval_strategy="no",             # disable evaluation
    per_device_train_batch_size=2,
    num_train_epochs=2,
    logging_dir="./logs",
    save_total_limit=1,
    save_strategy="epoch"
)

# 6️⃣ Initialize trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_data["train"]
)

# 7️⃣ Start training
trainer.train()

# 8️⃣ Save the fine-tuned model
model.save_pretrained("./drchatbot-model")
tokenizer.save_pretrained("./drchatbot-model")

print("\n✅ Training complete! Custom DrChatbot model saved in './drchatbot-model'")
