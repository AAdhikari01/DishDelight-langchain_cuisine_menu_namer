from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
api_key=os.environ.get['API']
# Set your API key
os.environ["GROQ_API_KEY"] = "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"

# Initialize LLM
llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0.6)
def generate_restaurant_name_and_items(cuisine):
    # Prompt for restaurant name + meaning
    prompt_name = PromptTemplate(
        input_variables=['cuisine'],
        template=(
            "Give me a fancy {cuisine} restaurant name, and explain its meaning or why it works in 1 sentence. "
            "Return in the format: Name - Meaning."
        )
    )
    name_chain = prompt_name | llm

    # Prompt for menu
    prompt_menu = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest me a concise menu (just dish names in English) for the restaurant called {restaurant_name}."
    )
    menu_chain = prompt_menu | llm

    # Generate restaurant name + meaning
    name_meaning_text = name_chain.invoke({"cuisine": cuisine}).content.strip()
    if " - " in name_meaning_text:
        restaurant_name, meaning = [x.strip() for x in name_meaning_text.split(" - ", 1)]
    else:
        restaurant_name = name_meaning_text
        meaning = ""

    # Generate menu
    menu_text = menu_chain.invoke({"restaurant_name": restaurant_name}).content.strip()
    menu_items = [item.strip() for item in menu_text.split(",") if item.strip()]

    return {
        "restaurant_name": restaurant_name,
        "meaning": meaning,
        "menu_items": menu_items
    }
