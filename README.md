# ChatGPT API Client

This Python script interacts with the OpenAI ChatGPT API. It allows users to send system and user prompts to ChatGPT, fetch the responses, and optionally format the responses in JSON mode.

## Requirements

- Python 3.7+
- Required libraries: `argparse`, `requests`, `json`, `os`, `sys`

## Installation

1. Clone the repository (or download the code):
    ```sh
    git clone <repository_url>
    cd <directory>
    ```

2. Install required packages:
    ```sh
    pip install requests
    ```

## Usage

1. **Prepare your API Key**: 
    Obtain an API key from OpenAI. The API key can be provided either as a command line argument or via an environment variable named `OPENAI_API_KEY`.

2. **Run the script with necessary arguments**:
    ```sh
    python chatgpt_client.py --system-prompt "Your system prompt" --user-prompt "Your user prompt with {{contents}}" [--api-key "Your OpenAI API key"] [--json-mode]
    ```

### Arguments

- `--system-prompt`: (Required) The system-level prompt for ChatGPT.
- `--user-prompt`: (Required) The user-level prompt template containing `{{contents}}` as a placeholder for standard input content.
- `--api-key`: (Optional) Your OpenAI API key. If not provided, the script will look for the `OPENAI_API_KEY` environment variable.
- `--json-mode`: (Optional) Enable JSON mode for the response. If this flag is set, the API response will be formatted as a JSON object.

### Example

Assuming you have saved the above code in a file named `chatgpt_client.py`:

```sh
echo "Your input content" | python chatgpt_client.py --system-prompt "You are a helpful assistant." --user-prompt "Please summarize the following: {{contents}}" --api-key "your_api_key" --json-mode

# concrete example
cat ./chatgpt_client.py | python3 ./chatgpt_client.py --system-prompt "You are helpful assistant." --user-prompt "Please create a README.md in English with the following code. <code>{{contents}}</code>" --api-key "xxxxxxxxxx" > README.md
```

### Environment Variable

You can set the environment variable `OPENAI_API_KEY` to store your API key:
```sh
export OPENAI_API_KEY="your_api_key"
```

### Error Handling

- If the API key is not provided either via command line argument or environment variable, the script will print an error message and exit.
- If the API returns an error, the script will print the error message and status code.

## Note

This script uses the `gpt-4o` model for interaction. Modify the `model` parameter in the `data` dictionary if you want to use a different model available in your API subscription.

## License

This project is licensed under the MIT License.

