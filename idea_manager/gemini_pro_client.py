from vertexai.preview.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models


class GeminiProClient:

    def generate_output(self, prompt):
        model = GenerativeModel("gemini-pro")
        response = model.generate_content(
            prompt,
            generation_config={
                "max_output_tokens": 2048,
                "temperature": 0.9,
                "top_p": 1
            },
            safety_settings={
                generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            },
            stream=False,
        )

        return response.text
