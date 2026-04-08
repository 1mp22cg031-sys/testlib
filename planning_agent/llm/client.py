from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class LLMClient:
    def __init__(self, model_name="mistralai/Mistral-7B-Instruct-v0.1"):
        print("🔄 Loading Mistral 7B...")

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )

        print(f"✅ Model loaded on {self.device}")

    def generate(self, prompt, max_tokens=300):
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=0.6,
            top_p=0.9
        )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)