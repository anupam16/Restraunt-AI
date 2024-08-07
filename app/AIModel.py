from langchain_openai import ChatOpenAI
import os


class AiModelHandler:
 
    @staticmethod
    def get_llm():
        try:
            
             llm = ChatOpenAI(api_key="")
             
             return llm
            
        except Exception as e:          
            print("Model error - ",e)
            raise e