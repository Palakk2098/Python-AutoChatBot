import pyautogui
import pyperclip
import time
from openai import OpenAI


client = OpenAI(
    api_key="#####"
)

# Define coordinates (adjust as needed)
start_x, start_y = 1026, 1412  # Starting point to click
middle_x, middle_y = 1026, 244      # Point of selection
end_x, end_y = 1131, 1321  # Ending point of the selection
deselect_x, deselect_y = 1994, 281


def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):

    # Split the chat into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]

    if sender_name in messages:
        return True

    return False


# Click on the starting icon
pyautogui.click(start_x,start_y)
time.sleep(1)
while True:
 

    # Select content by dragging
    pyautogui.moveTo(middle_x, middle_y)
    pyautogui.dragTo(end_x, end_y, duration=1, button="left")


    # Copy selected content to clipboard
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(deselect_x,deselect_y)
    time.sleep(1)  # Wait for the content to copy

    # Retrieve the copied content
    chatHistory = pyperclip.paste()
    print(f"Copied content: {chatHistory}")

    if(is_last_message_from_sender(chatHistory)):

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a person named Naruto who speaks Hindi as well as English. You are from India and is a coder. You analyze the chat history and respond like Naruto. Output should be the further chat from the request data as per the chat history."},
                {
                    "role": "user",
                    "content": chatHistory
                }
            ]
        )

        response = completion.choices[0].message.content


        # Copy the text which is the response
        pyperclip.copy(response)

        # Click the coordinates 
        pyautogui.click(1808,1328)
        time.sleep(1)

        # Paste the text
        pyautogui.hotkey('ctrl',"v")
        time.sleep(1)

        # Press Enter
        pyautogui.press("enter")

        print("Content copied and pasted successfully!")
