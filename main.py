
import os

from llama_caller import LLMCaller
from prompt_builder import PromptBuilder

from fastapi import FastAPI, Query



app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Add this block to your FastAPI app initialization
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Update this to match your frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Initialize PromptBuilder and LLMCaller
prompt_builder = PromptBuilder('long_prompt_string.txt')
llm_caller = LLMCaller(api_key=os.environ.get("GROQ_API_KEY_AFFIRMATIONS_HELPER"))


@app.get("/")
async def get_goal_from_front_end(goal: str = Query(...)):
    """
    HTTP GET endpoint to process a goal and return a response.
    """
    try:
        # Log received goal
        print(f"***********GOAL: {goal}")

        # Build a prompt and get the Llama 3 response
        prompt = prompt_builder.build_prompt([goal])
        output_file_name = llm_caller.chat(prompt)

        # Read the output from the file
        with open(output_file_name, 'r') as file:
            output_text = file.read()

        return {"goal": goal, "affirmation": output_text}
    except Exception as e:
        return {"error": str(e)}

def main():
    def build(self):
        
        self.prompt_builder = PromptBuilder('long_prompt_string.txt')
        self.llm_caller = LLMCaller(api_key=os.environ.get("GROQ_API_KEY_AFFIRMATIONS_HELPER"))

        data = get_goal_from_front_end()

# FastAPI runs as a server, no need for a `main()` function
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)