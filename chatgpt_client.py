import argparse
import os
import sys
import requests
import json
import base64

def get_args():
    parser = argparse.ArgumentParser(description="ChatGPT API client")

    parser.add_argument("--system-prompt", type=str, required=True, help="System prompt for ChatGPT")
    parser.add_argument("--user-prompt", type=str, required=True, help="User prompt template containing {{contents}}")
    parser.add_argument("--api-key", type=str, help="API key for OpenAI")
    parser.add_argument("--json-mode", action="store_true", help="Enable JSON mode for response")
    parser.add_argument("--images", type=str, nargs="*", default=[], help="")
    parser.add_argument("--image-urls", type=str, nargs="*", default=[], help="")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="LLM model")

    return parser.parse_args()

def get_api_key(args):
    if args.api_key:
        return args.api_key
    return os.getenv("OPENAI_API_KEY")

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def _build_base64_image_obj(base64_image):
    return {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}",
            "detail": "low"
        }
    }

def _build_image_url_obj(image_url):
    return {
        "type": "image_url",
        "image_url": {
            "url": image_url,
            "detail": "low"
        }
    }

def build_content(user_prompt, image_urls, images):
    content = []

    content.append({ "type": "text", "text": user_prompt })

    for image_url in image_urls:
        content.append(_build_image_url_obj(image_url))

    for image in images:
        content.append(_build_base64_image_obj(encode_image_to_base64(image)))

    return content


def build_system_message(system_prompt):
    return {
        "role": "system",
        "content": system_prompt
    }

def build_user_message(user_prompt, image_urls, images):
    _image_urls = image_urls if [] is None else image_urls
    _images = images if [] is None else images

    return {
        "role": "user",
        "content": build_content(user_prompt, image_urls, images)
    }

def main():
    args = get_args()
    api_key = get_api_key(args)

    if not api_key:
        print("Error: API key is required either as an argument or in the OPENAI_API_KEY environment variable.")
        sys.exit(1)

    input_content = sys.stdin.read().strip()
    user_prompt = args.user_prompt.replace("{{contents}}", input_content)

    messages = [
        build_system_message(args.system_prompt),
        build_user_message(user_prompt, args.image_urls, args.images)
    ]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": args.model,
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

