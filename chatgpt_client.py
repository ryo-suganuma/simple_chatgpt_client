import argparse
import os
import sys
import requests
import json

def get_args():
    parser = argparse.ArgumentParser(description="ChatGPT API client")
    parser.add_argument("--system-prompt", type=str, required=True, help="System prompt for ChatGPT")
    parser.add_argument("--user-prompt", type=str, required=True, help="User prompt template containing {{contents}}")
    parser.add_argument("--api-key", type=str, help="API key for OpenAI")
    parser.add_argument("--json-mode", action="store_true", help="Enable JSON mode for response")
    return parser.parse_args()

def get_api_key(args):
    if args.api_key:
        return args.api_key
    return os.getenv("OPENAI_API_KEY")

def main():
    args = get_args()
    api_key = get_api_key(args)

    if not api_key:
        print("Error: API key is required either as an argument or in the OPENAI_API_KEY environment variable.")
        sys.exit(1)

    input_content = sys.stdin.read().strip()
    user_prompt = args.user_prompt.replace("{{contents}}", input_content)

    messages = [
        {"role": "system", "content": args.system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "gpt-4o",
        "messages": messages,
        "max_tokens": 4000
    }

    if args.json_mode:
        data["response_format"] = { "type": "json_object"  }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        if response_data.get('choices'):
            print(response_data['choices'][0]['message']['content'].strip())
        else:
            print("No response from OpenAI API.")
    else:
        print(f"Error fetching summary: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()

