import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample database table structure
products_table = {
    "mangoes": {"product_name": "mangoes", "tariff_rate": 10},
    "apples": {"product_name": "apples", "tariff_rate": 15},
    "bananas": {"product_name": "bananas", "tariff_rate": 8}
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
    for word in filtered_tokens:
        if word in products_table:
            product = word
            break
    
    # Generate SQL query based on the extracted information
    if product:
        sql_query = "SELECT tariff_rate FROM products WHERE product_name = '{}'".format(products_table[product]["product_name"])
        return sql_query
    else:
        return None

# Example usage
natural_language_question = "What is the tariff rate for mangoes?"
sql_query = generate_sql_query(natural_language_question)
print("Natural Language Question:", natural_language_question)
print("Generated SQL Query:", sql_query)
