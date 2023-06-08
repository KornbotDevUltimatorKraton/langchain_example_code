from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
secret_key="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"
llm = OpenAI(openai_api_key=secret_key)
text = "How to do trademark in USA?"
print(llm(text))
