from langchain_community.chat_models import QianfanChatEndpoint
from langchain.chains import ConversationChain
from chatbot.config import QIANFAN_AK,QIANFAN_SK
from langchain_core.prompts import PromptTemplate

class Chatbot:
    prompt_template = PromptTemplate.from_template("你是一个严谨的助手，善于向用户提供准确的信息。")
    def __init__(self):
        llm = QianfanChatEndpoint(model="Qianfan-Chinese-Llama-2-7B",qianfan_ak=QIANFAN_AK,qianfan_sk=QIANFAN_SK,
                                  prompt=Chatbot.prompt_template)
        self.conversation_chain = ConversationChain(llm=llm)
    def ask(self, message):
        response = self.conversation_chain.predict(input=message)
        # print(response)
        return response



if __name__ == "__main__":
    # 测试
    chatbot = Chatbot()
    print("res1:\n",chatbot.ask("记住一个变量：int a=10;"))
    # print("his1:\n",chatbot.gethistory().messages)
    print("res2:\n",chatbot.ask("变量a的值是多少？"))
    # print("his2:\n", chatbot.gethistory().messages)