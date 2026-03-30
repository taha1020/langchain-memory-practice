from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI()

memory = ConversationSummaryMemory(llm=llm)
conversation = ConversationChain(llm=llm, memory=memory)

print(conversation.run("I love AI and machine learning"))
print(conversation.run("What do I love?"))
