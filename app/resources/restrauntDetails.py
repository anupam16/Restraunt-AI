from flask_restful import Resource, reqparse
from flask import request, jsonify
from app.AIModel import AiModelHandler
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain
from ..prompts.prompts import restraunt_prompt,direction_prompt,hotel_details_prompt

class RestrauntDetails(Resource):
     def post(self):
             data=request.get_json()
             llm=AiModelHandler.get_llm()
            #  prompt = PromptTemplate(
            #               input_variables=['query','historyPayloads'],
            #               template=restraunt_prompt
            #           )
            #  chain = LLMChain(llm=llm, prompt=prompt)
             
            #  content = chain.run(city =data.get("city"), facilities=data.get("facilities") )
          #    content= llm.invoke("tell me the list restaurant n dehradun with a swimming pool")
            #  print("hola",content,data)
        #      return jsonify({"details":content})
             
             prompt1 = PromptTemplate(
             input_variables=["city", "facilities"],
             template=restraunt_prompt
             )
             chain1 = LLMChain(prompt=prompt1, llm=llm, output_key="hotel")
  
  
             prompt2 = PromptTemplate(
                 input_variables=["hotel"],
                 template=hotel_details_prompt
             )
             chain2 = LLMChain(prompt=prompt2, llm=llm, output_key="hotel_details")
  
  
             prompt3 = PromptTemplate(
                 input_variables=["hotel_details", "current_location"],
                 template=direction_prompt
             )
             chain3 = LLMChain(prompt=prompt3, llm=llm, output_key="directions")

             sequential_chain = SequentialChain(
             chains=[chain1, chain2, chain3],
             input_variables=["city", "facilities", "current_location"],
             output_variables=["hotel_details", "directions","hotel"]
             )
             input_data = {
                "city": data.get("city"),
                "facilities": data.get("facilities"),
                "current_location": data.get("current_location")
             }

#
             result = sequential_chain(input_data)


             print("Hotel Details:", result["hotel"])
             print("Directions:", result["directions"])
             
            #  chain22={"hotel":chain11}|prompt2|llm
            #  chain33={"hotel_details":chain22}|prompt3|llm
             se= prompt1|llm| (lambda input: {"hotel":input} )|prompt2|llm|(lambda input:{"current_location":data.get("current_location"),"hotel_details":input} )|prompt3|llm
             print("test", se.invoke(input_data))

             return jsonify(result)


 

