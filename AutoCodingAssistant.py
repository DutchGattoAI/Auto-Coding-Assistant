import openai

openai.api_key = 'your-api-key'

class CodingAssistant:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": "You are a helpful coding assistant."},
        ]

    def ask(self, question):
        self.messages.append({"role": "user", "content": question})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            max_tokens=150
        )

        answer = response.choices[0].message['content']
        self.messages.append({"role": "assistant", "content": answer})

        return answer

    def correct(self):
        # Let the AI self-evaluate its response
        self.messages.append({"role": "user", "content": "Did you complete the task correctly?"})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            max_tokens=150
        )

        evaluation = response.choices[0].message['content']
        self.messages.append({"role": "assistant", "content": evaluation})

        return evaluation

# Usage:
assistant = CodingAssistant()

# Asking the assistant to write some code
response = assistant.ask("Can you write a Python function to calculate the factorial of a number?")
print(response)

# Let the AI self-evaluate its response
evaluation = assistant.correct()
print(evaluation)

# If the assistant's self-evaluation wasn't positive, you can ask it to try again
if "no" in evaluation.lower():
    response = assistant.ask("Can you try again?")
    print(response)
