import json
from typing import TYPE_CHECKING, Optional

from .base import AIProvider

if TYPE_CHECKING:
    from ..config import Config


class OllamaProvider(AIProvider):
    """Ollama provider"""

    def __init__(self, config: "Config", custom_prompts_path: Optional[str] = None):
        super().__init__(config, custom_prompts_path)
        try:
            from ollama import Client

            self.client = Client(host=config.ollama_api_url)
        except ImportError:
            raise ImportError(
                "Ollama library is not installed. Please install it with 'pip install ollama'."
            )

    def is_configured(self) -> bool:
        """Check if the provider is configured."""
        return bool(self.config.ollama_model)

    def generate_commit_message(
        self,
        diff_content: str,
        language: Optional[str] = None,
        branch_name: Optional[str] = None,
        previous_commits: Optional[str] = None,
        additional_context: Optional[str] = None,
    ) -> str:
        """Generate a commit message using Ollama."""
        language = language or self.config.default_lang or "en"
        prompt = self._create_base_prompt(
            diff_content, language, branch_name, previous_commits, additional_context
        )

        max_attempts = 3
        attemps = 0
        while attemps < max_attempts:
            try:
                response = self.client.chat(
                    model=self.config.ollama_model,
                    messages=[
                        {
                            "role": "system",
                            "content": self.prompts.SYSTEM_PROMPT,
                        },
                        {
                            "role": "user",
                            "content": prompt,
                        },
                    ],
                )
                response_content = response.message.content.strip()
                return json.loads(self._clean_markdown_json_block(response_content))

            except Exception:
                attemps += 1
        if attemps == max_attempts:
            raise Exception(
                f"Error generating commit message with Ollama after {max_attempts} attempts"
            )
