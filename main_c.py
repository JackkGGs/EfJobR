import google.generativeai as genai
import random
from config import *

# --------------------------------------------------------------------------------
# AI Configuration
# --------------------------------------------------------------------------------

# Replace with your Gemini API key
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-lite')

# --------------------------------------------------------------------------------
# Helper Function
# --------------------------------------------------------------------------------

def format_recommendation_as_text(ai_text):
    """
    Cleans up the AI's response for better readability in the console.
    Removes markdown formatting that won't display correctly.
    """
    # Remove markdown bolding and headings
    text = ai_text.replace("**", "").replace("### ", "").replace("*", "")
    return text

# --------------------------------------------------------------------------------
# Main Program Loop
# --------------------------------------------------------------------------------

def main():
    """Main function to run the bot in the command line."""
    print("Welcome to EfJobR Console Edition! 👋")
    print("Explain your interests. Input 'exit' to exit out.")

    while True:
        user_input = input("Input your response: ")
        if user_input.lower() == 'exit':
            print("See ya! 👋")
            break

        print("EfJobR: Hmm, I'm thinking... 🧠")
        
        try:
            # Generate a random temperature
            random_temp = round(random.uniform(0.1, 1.0), 1)

            # Prompt for the AI
            prompt = f"""
            Your name is EfJobR. Your task is to give humans recommendations on jobs and possible open recruitments.
                
                Your message musn't exceed 499 characters!
                You're allowed to embed links here.
                Keep an eye on "User's message" by the way. Adjust your response by translating it to the language the user used on the user's message.
                On the end of the message, add "Did this help?" or similar messages depending on the language the user used

                Keep this format and ONLY this format (Translate for multilingual cases EXCEPT the words before ":"):
                Hmm..
                Alright,
            
                - Career: [Career Name]
                - Description: [A simple description of the career]
                - Required Skills: [A list of required skills, use comas]
                - Demo Projects: [A simple demo project to hone the skills]
                - Resources: [Embed 1-2 links here]

                User's message: {user_input}
            """

            # Get the response from the AI
            response = model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=random_temp,
                    max_output_tokens=300
                )
            )

            # Format and print the response
            formatted_response = format_recommendation_as_text(response.text)
            print("\n" + "="*50)
            print(formatted_response)
            print("="*50 + "\n")

        except Exception as e:
            print(f"Sorry, there seems to be an error handling this request. Error: {e}")

if __name__ == "__main__":
    main()