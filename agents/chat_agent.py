from haystack.components.agents import Agent
from haystack.components.generators.chat import HuggingFaceAPIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack.tools import ComponentTool
from haystack.components.websearch import SerperDevWebSearch
from haystack.utils import Secret

search_tool = ComponentTool(component=SerperDevWebSearch())

agent = Agent(
    chat_generator=HuggingFaceAPIChatGenerator(
        api_type="serverless_inference_api",
        api_params={"model": "meta-llama/Llama-3.1-8B-Instruct"}, # Thử đổi sang Llama 3.1
        token=Secret.from_env_var("HF_API_TOKEN"),
    ),
    tools=[search_tool],
    system_prompt="You are a helpful assistant that can search the web for information.",
)

result = agent.run(messages=[ChatMessage.from_user("What is Haystack AI?")])

print(result["last_message"].text)