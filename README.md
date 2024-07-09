# ChatGPT API Client

This is a command-line tool to interact with OpenAI's ChatGPT API.

## Features

- Send system and user prompts to ChatGPT.
- Include images (both local and online) as additional input.
- Support JSON mode for receiving structured responses.

## Requirements

- Python 3.6 or later
- `requests` library

You can install the `requests` library using:

```bash
pip install requests
```

## Installation

1. Clone the repository or download the script.
2. Make sure you have Python installed.
3. Install the required libraries by running:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line with appropriate arguments.

```bash
python script.py --system-prompt "Your system prompt" --user-prompt "Hello, {{contents}}" --api-key "your-api-key"
```

### Arguments

- `--system-prompt`: System prompt for ChatGPT. (Required)
- `--user-prompt`: User prompt template containing `{{contents}}`. (Required)
- `--api-key`: API key for OpenAI. You can either pass it as an argument or set it as an environment variable `OPENAI_API_KEY`.
- `--json-mode`: Enable JSON mode for response.
- `--images`: Paths to local images to be included in the request. (Optional)
- `--image-urls`: URLs of online images to be included in the request. (Optional)

### Example

To send a system and user prompt along with an image URL:

```bash
python script.py --system-prompt "System prompt" --user-prompt "User prompt with content: {{contents}}" --api-key "your-api-key" --image-urls "https://example.com/image1.jpg"
```

### Environment Variable

Alternatively, you can set the `OPENAI_API_KEY` environment variable for the API key:

```bash
export OPENAI_API_KEY="your-api-key"
```

Then run the script without the `--api-key` argument:

```bash
python script.py --system-prompt "Your system prompt" --user-prompt "Hello, {{contents}}"
```

## Input

The script will read from standard input (`stdin`). You can pipe input to the script or provide input interactively.

### Example with Piping Input

```bash
echo "This is the content" | python script.py --system-prompt "System prompt" --user-prompt "User prompt with content: {{contents}}" --api-key "your-api-key"
```

## Output

The response from ChatGPT will be printed to the standard output (`stdout`).

## Error Handling

If there is an error (e.g., missing API key or invalid request), the script will print an error message and exit with a non-zero status.

## License

This project is licensed under the MIT License.

