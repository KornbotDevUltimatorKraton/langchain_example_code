from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
secret_key="Put your secretkey from openAI website"
llm = OpenAI(openai_api_key=secret_key)
text = "How to do trademark in USA?"
print(llm(text))
