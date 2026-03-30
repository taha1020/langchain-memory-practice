from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI()

memory = ConversationBufferWindowMemory(k=1)
conversation = ConversationChain(llm=llm, memory=memory)

print(conversation.run("I live in Pakistan"))
print(conversation.run("Where do I live?"))
