class PromptBuilder:
    def __init__(self, file_path: str):
        self.long_string = self._read_long_string_from_file(file_path)

    def _read_long_string_from_file(self, file_path: str) -> str:
        with open(file_path, 'r') as file:
            return file.read()

    def build_prompt(self, goals: list) -> str:
        goal_section = self._build_goal_section(goals)
        return self.long_string + goal_section

    def _build_goal_section(self, goals: list) -> str:
        goal_strings = [f"Goal {i+1}: {goal}" for i, goal in enumerate(goals)]
        return "\n".join(goal_strings)