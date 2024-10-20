import json
import os

from dotenv import load_dotenv
from typing import Optional, List, Mapping, Any

from tools.historical_data_tool import historical_data_tool_func
from tools.search_engine import use_search_engine

load_dotenv("/Users/stas_chi/Documents/Projects/Izba AI/izba-ai/backend/.env")

from openai import OpenAI
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.core.llms import (
    CustomLLM,
    CompletionResponse,
    CompletionResponseGen,
    LLMMetadata,
)
from llama_index.core.llms.callbacks import llm_completion_callback
from llama_index.core import Settings

class NebiusLLM(CustomLLM):
    context_window: int = 128e3
    num_output: int = 8192
    model_name: str = "nebius"
    dummy_response: str = "Dummy response"

    @property
    def metadata(self) -> LLMMetadata:
        """Get LLM metadata."""
        return LLMMetadata(
            context_window=self.context_window,
            num_output=self.num_output,
            model_name=self.model_name,
        )

    @llm_completion_callback()
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        client = OpenAI(
            base_url=os.environ.get("NEBIUS_BASE_URL"),
            api_key=os.environ.get("NEBIUS_API_KEY"),
        )

        completion = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-405B-Instruct",
            messages=[
            {
                "role": "system",
                "content": prompt
            }
            ],
            temperature=0,
            max_tokens=8192,
            top_p=0.9
        )

        return CompletionResponse(
            text=completion.choices[0].message.content
        )
    
    @llm_completion_callback()
    def stream_complete(
        self, prompt: str, **kwargs: Any
    ) -> CompletionResponseGen:
        response = ""
        for token in self.dummy_response:
            response += token
            yield CompletionResponse(text=response, delta=token)

llm = NebiusLLM()

historical_data_tool = FunctionTool.from_defaults(fn=historical_data_tool_func)
search_engine_tool = FunctionTool.from_defaults(fn=use_search_engine)

agent = ReActAgent.from_tools([historical_data_tool,search_engine_tool], llm=llm, verbose=True)