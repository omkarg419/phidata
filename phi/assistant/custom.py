from typing import Optional

from phi.task.llm import LLMTask
from phi.assistant import Assistant


class CustomAssistant(Assistant):
    def get_system_prompt(self) -> Optional[str]:
        """Return the system prompt for the assistant"""
        return None

    @property
    def llm_task(self) -> LLMTask:
        _llm_task = super().llm_task

        # Use the custom assistant system prompt if the system prompt is not set
        if self.system_prompt is None or self.system_prompt_function is None:
            assistant_system_prompt = self.get_system_prompt()
            if assistant_system_prompt is not None:
                _llm_task.system_prompt = assistant_system_prompt

        return _llm_task
