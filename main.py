import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',

}

conversation_history = []


def response_generator(prompt):
        conversation_history.append(prompt)
        prompt_full = "\n".join(conversation_history)
        data = {
            "model": "mistral",
            "stream": False,
            "prompt": "Why is the sky blue?"

        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
                response_text = response.text
                data = json.loads(response_text)
                actual_response = data["response"]
                conversation_history.append(actual_response)
                print(actual_response)
        else:
                print("Error:", response.status_code, response.text)
                

iface = gr.Interface(
    fn=response_generator,
    inputs= gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
    outputs="text"
)

iface.launch(share=True)

