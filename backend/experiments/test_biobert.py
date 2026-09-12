import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split


file_path = "dataset.csv" 
df = pd.read_csv(file_path)


print(df.head())


dataset = Dataset.from_pandas(df)

model_id = "dmis-lab/biobert-base-cased-v1.1" 
tokenizer = AutoTokenizer.from_pretrained(model_id)


def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True, max_length=128)


dataset = dataset.map(tokenize_function, batched=True)


train_dataset, eval_dataset = dataset.train_test_split(test_size=0.2).values()

model = AutoModelForSequenceClassification.from_pretrained(model_id, num_labels=len(df['label'].unique()))

training_args = TrainingArguments(
    output_dir="./results",          
    num_train_epochs=3,              
    per_device_train_batch_size=8,   
    per_device_eval_batch_size=16,   
    logging_dir="./logs",            
    logging_steps=100,               
    save_steps=1000,                
    save_total_limit=1,              
)

trainer = Trainer(
    model=model,                         
    args=training_args,                 
    train_dataset=train_dataset,         
    eval_dataset=eval_dataset            
)


trainer.train()


results = trainer.evaluate()
print(results)
