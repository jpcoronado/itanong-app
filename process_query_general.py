import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample database table structure
products_table = {
    "mangoes": {"product_name": "mangoes", "tariff_rate": 10, "origin": "India", "category": "fruit"},
    "apples": {"product_name": "apples", "tariff_rate": 15, "origin": "USA", "category": "fruit"},
    "bananas": {"product_name": "bananas", "tariff_rate": 8, "origin": "Ecuador", "category": "fruit"}
}

# Function to convert natural language question to SQL query
def generate_sql_query(natural_language_question):
    # Tokenize the question
    tokens = word_tokenize(natural_language_question.lower())
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Extract key information from the question
    product = None
    property_of_interest = None
    for word in filtered_tokens:
        if word in products_table:
            product = word
        elif product and word in products_table[product]:
            property_of_interest = word
            break
    
    # Generate SQL query based on the extracted information
    if product and property_of_interest:
        sql_query = "SELECT {} FROM products WHERE product_name = '{}'".format(property_of_interest, products_table[product]["product_name"])
        return sql_query
    elif not property_of_interest:
        return "Please specify a valid property."
    else:
        return "Product not found."

# Example usage
natural_language_question = "What is the origin of mangoes?"
sql_query = generate_sql_query(natural_language_question)
print("Natural Language Question:", natural_language_question)
print("Generated SQL Query:", sql_query)
