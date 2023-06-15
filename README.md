# Auto-Coding-Assistant

(First test of an Auto Coding Assistant with OpenAI GPT)

# AI Auto Coding Assistant

This repository contains a simple implementation of an AI coding assistant using OpenAI's GPT-3 model. The assistant can generate code snippets and self-evaluate its performance. Please note the following important points before running this script:

## Requirements

- OpenAI API Key: This script uses the OpenAI API, which requires an API key. You'll need to replace `'your-api-key'` in the code with your actual OpenAI API key.

## Warnings

- **Cost**: The OpenAI API is not free. Every time you run the script, it makes requests to the API which costs money. The cost is based on the number of tokens processed. Please check OpenAI's pricing details for more information.

- **Security**: Be sure to handle your API keys securely. Do not expose them in public repositories or any places where unauthorized users might gain access.

- **Quality and Limitations**: The output of this script depends on the GPT-3 model, which has limitations. It doesn't perfectly understand context or remember past requests. The quality of the generated code may vary, and the script doesn't verify or execute the generated code.

- **Usage Limitations**: OpenAI sets limits on the number of tokens that can be processed in a single API call and the rate of API calls. Very long prompts or very frequent requests may fail due to these limitations.

- **Responsibility**: As the code provider, I am not responsible for any charges you may incur from OpenAI, any misuse of your API key, or any consequences of the code produced by the AI.

## Usage

First, replace `'your-api-key'` with your actual OpenAI API key. Then, run the script:

```
python AutoCodingAssistant.py
```

The script will prompt the AI to generate code snippets and self-evaluate its performance. If the AI determines it did not complete the task correctly, it will try again.
