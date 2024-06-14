from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import os

from llama_caller import LLMCaller
from prompt_builder import PromptBuilder

class MainApp(App):
    def build(self):
        self.prompt_builder = PromptBuilder('long_prompt_string.txt')
        self.llm_caller = LLMCaller(api_key=os.environ.get("GROQ_API_KEY_AFFIRMATIONS_HELPER"))

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.label = Label(text="Enter your goals below:")
        self.goals_inputs = [TextInput(hint_text=f"Goal {i+1}") for i in range(3)]

        self.button = Button(text="Generate Affirmations", on_press=self.on_button_click)

        layout.add_widget(self.label)
        for input_box in self.goals_inputs:
            layout.add_widget(input_box)
        layout.add_widget(self.button)

        return layout

    def on_button_click(self, instance):
        goals = [input_box.text for input_box in self.goals_inputs if input_box.text]
        if not goals:
            self.label.text = "Please enter at least one goal."
            return

        prompt = self.prompt_builder.build_prompt(goals)
        output_file_name = self.llm_caller.chat(prompt)

        with open(output_file_name, 'r') as file:
            output_text = file.read()
        self.label.text = output_text

if __name__ == '__main__':
    app = MainApp()
    app.run()