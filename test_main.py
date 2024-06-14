import unittest
from unittest.mock import patch, mock_open
from main import MainApp
from llama_caller import LLMCaller
from prompt_builder import PromptBuilder
from sample_goals import sample_goals
import os

class TestMainApp(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    @patch('llama_caller.LLMCaller.chat')
    def test_app_with_sample_goals(self, mock_chat, mock_file):
        # Setup mock return values
        mock_chat.return_value = "affirmations_20230101010101.md"
        mock_file.return_value.read.return_value = "Mocked affirmation content"

        # Setup app
        app = MainApp()
        app.prompt_builder = PromptBuilder('long_prompt_string.txt')
        app.llm_caller = LLMCaller(api_key=os.environ.get("GROQ_API_KEY_AFFIRMATIONS_HELPER"))

        # Simulate entering goals
        for i, input_box in enumerate(app.goals_inputs):
            input_box.text = sample_goals[i+1]

        # Simulate button click
        app.on_button_click(None)

        # Assertions
        mock_chat.assert_called_once()
        self.assertIn("Mocked affirmation content", app.label.text)

if __name__ == '__main__':
    unittest.main()