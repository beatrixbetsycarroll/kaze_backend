from groq import Groq
import datetime

class LLMCaller:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def chat(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            # model="llama3-8b-8192",
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_dir_name = "artifacts"
        output_file_name = f"{output_dir_name}/affirmations_{timestamp}.md"

        with open(output_file_name, 'w') as output_file:
            for chunk in completion:
                if hasattr(chunk.choices[0], 'delta'):
                    content = chunk.choices[0].delta.content or ""
                    output_file.write(content)
                    print(content, end="")  # Print to console as well

        return output_file_name