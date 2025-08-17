from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Force model onto CPU
model = AutoModelForCausalLM.from_pretrained(model_name, device_map=None).to("cpu")

# Keep conversation history
conversation = [{"role": "system", "content": "You are a helpful assistant."}]

print("💬 TinyLlama Chat on CPU (type 'quit' to exit)\n")

while True:
    # Get user input
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break

    # Add user message
    conversation.append({"role": "user", "content": user_input})

    # Format with chat template
    chat_text = tokenizer.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(chat_text, return_tensors="pt").to("cpu")

    # Generate response
    outputs = model.generate(**inputs, max_new_tokens=200, do_sample=True, temperature=0.7)

    # Decode
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Extract only assistant part (after last user input)
    assistant_reply = response.split(user_input)[-1].strip()

    print(f"TinyLlama: {assistant_reply}\n")

    # Add assistant reply to conversation history
    conversation.append({"role": "assistant", "content": assistant_reply})
