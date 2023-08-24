import os
import datetime
import re
import openai

# Set up the authentication (Use your API key)
openai.api_key = "YOUR-API-KEY-HERE"

def get_time_of_day():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Morning"
    elif current_hour < 18:
        return "Afternoon"
    else:
        return "Evening"
    

def clean_and_chunk_chatlog(file_path, max_chunk_length=8000):
    '''Clean the chat log to remove date and time stamps and divide it into manageable chunks.'''
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            chat_log = file.readlines()
        print("File opened successfully.")
    except Exception as e:
        print(f"Error opening file: {e}")
        return []
    
    # Clean the chat log
    cleaned_chat = []
    for line in chat_log:
        cleaned_line = re.sub(r"^\[\d{1,2}:\d{1,2} [APMapm]*\s?-?\s?", "", line)
        cleaned_line = re.sub(r"\[\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{1,2}:\d{1,2}\]", "", cleaned_line)
        cleaned_line = cleaned_line.strip()
        if cleaned_line:
            cleaned_chat.append(cleaned_line)
    cleaned_chat_text = "\n".join(cleaned_chat)
    
    # Divide the chat log into chunks
    chunks = []
    while len(cleaned_chat_text) > max_chunk_length:
        split_index = cleaned_chat_text[:max_chunk_length].rfind("\n")
        if split_index == -1:
            split_index = max_chunk_length
        chunks.append(cleaned_chat_text[:split_index].strip())
        cleaned_chat_text = cleaned_chat_text[split_index:]
    if cleaned_chat_text:
        chunks.append(cleaned_chat_text.strip())
    
    print(f"File split into {len(chunks)} chunks.")
    return chunks

def generate_recap(chat_chunk):
    '''Generate a recap for the given chat chunk using OpenAI.'''
    print("Sending chunk to OpenAI for processing...")
    # Define the prompt for the API request
    prompt = "🌞 Please provide a bulleted GPT Recap for the following chat in the format of points capturing main events, discussions, and banter. Ensure you don't focus too much on one individual member and stylize your response with emojis. 🌞\n\n"
    input_content = prompt + chat_chunk
    
    # Make the API request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input_content}],
        temperature=0.7,
        max_tokens=400
    )
    recap = response.choices[0].message.content
    print("Recap generated for chunk.")
    return recap

def refine_summary(summary):
    '''Refine the summary for better consistency and engagement.'''
    print("Refining the overall summary for consistency...")
    prompt = "🌞 Please refine the following summary for a consistent and stylized format. Ensure it's succinct and engaging, capturing the essence of the discussion. Start and finish each line with emoji's. Don't editorialise too much. 🌞\n\n"
    input_content = prompt + summary
    
    # Make the API request
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": input_content}],
        temperature=0.8,
        max_tokens=1200
    )
    refined_summary = response.choices[0].message.content
    print("Refined summary generated.")
    return refined_summary

def main():
    '''Main function to generate and display the chat recap.'''
    chat_file_path = input("Enter path to your WhatsApp chat log (.txt file): ")
    chat_chunks = clean_and_chunk_chatlog(chat_file_path)
    if not chat_chunks:
        print("Exiting due to errors.")
        return
    recaps = [generate_recap(chunk) for chunk in chat_chunks]
    
    # Combine all the recaps
    final_recap = recaps[0]
    for recap in recaps[1:]:
        content = "\n".join(recap.split("\n")[1:-2])
        final_recap += "\n" + content
    
    # Refine the combined recap for a better presentation
    final_refined_recap = refine_summary(final_recap)
    
    # Display the final refined recap
    header = f"🤖🤖GPT Recap Generated {datetime.datetime.now().strftime('%d %b %Y')} {get_time_of_day()}🤖🤖"
    print(header)
    print("\n" + final_refined_recap)

if __name__ == "__main__":
    main()
