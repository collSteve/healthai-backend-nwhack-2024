from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

models = {
    "gpt-4-turbo": "gpt-4-1106-preview"
}

system_prompts = [
    "You are a health professional responding to a medical emergency. You are talking to a patient and you are trying to help them."
    + "Give your response in JSON format in the following way: {'reponse': your response and advice for the patient, 'questions': additional question you would ask the patient to assess their situation}",
]

# Post request for health instruction
def health_instruction(request):

    if request.method == 'POST':
        my_data = request.POST.get('user_input', "")
        if (my_data == ""):
            return JsonResponse({"status": "error", "message": "Please put in a valid input"}, status=400)

        completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_prompts[0]},
            {"role": "user", "content": "my heart hurts"},
        ]
        )
        print(completion.choices[0].message.content)

        response = {"status": "success", "response": completion.choices[0].message.content}
        return JsonResponse(response, status=200)
    else:
        return render(request, 'health_instruction.html')