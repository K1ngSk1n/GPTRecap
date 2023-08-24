# GPTRecap - Automated Chat Summaries 🤖✨
GPTRecap is a Python script that leverages the power of OpenAI's GPT-4 model to automatically generate concise, stylized summaries of chat logs. Whether you missed a day of conversation in your group chat or just need a quick recap, GPTRecap has got you covered!

Features
- Reads raw chat logs and cleans them.
- Splits large chat logs into manageable chunks.
- Generates bulleted summaries for each chunk.
- Refines the overall summary for a consistent and engaging format.
- Provides date and time-of-day specific headers for context.

Requirements
Python 3.x
OpenAI Python Client (You can install it using pip install openai)

Usage
Clone or download the repository.
Navigate to the directory containing chat_recap_0.3.py.
Run the script using the command: python chat_recap_0.3.py.
Follow the on-screen prompts and provide the path to your chat log file.
Enjoy your automated chat summary!

Configuration
Before running the script, ensure you set up your OpenAI API key in the script:
"openai.api_key = "YOUR_API_KEY_HERE""
Replace YOUR_API_KEY_HERE with your actual OpenAI API key.

Note
The script currently supports chat logs that have WhatsApp specific timestamp formats. Adjustments might be required for different formats.
The OpenAI API may incur costs depending on the number of tokens processed and the pricing model at the time of use. Ensure you're aware of any potential charges.

Future Improvements
- Support for additional chat log formats.
- Integration with cloud storage for direct chat log uploads.
- A web-based interface for an enhanced user experience.
