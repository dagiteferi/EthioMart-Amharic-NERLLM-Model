
import re

# List of B-PRODUCT items
b_product_items = [
    'መዓዛ', 'ፎን', 'ቁም ሳጥን', 'ማቅረቢያ', 'ማጨሻ', 'ሞልዶች', 'ማስቀመጫ', 'ከረጢት', 'የውሃ ጆግ', 'ድስቶች', 'ሳህን', 'ማፍሊያ',
    'መቀነሻዎች', 'ገንዳ', 'ፋኖች', 'ድንኳን', 'መደርደሪያ', 'መሰንጠቂያ', 'መከላከያ', 'ዕቃ', 'ማብሰያ', 'ይይዛል', 'ፔርሙዝ', 'ማስጪያ',
    'ጋቻ', 'ቶንዶስ', 'መፍጪያ', 'ጆጎቹ', 'ምሳ ዕቃ', 'መስታወት', 'ማስቀመጫ', 'መጋገሪያ', 'ትራስ', 'መስሪያ', 'ድስት', 'ቄጤማ', 'ማንኪያዎች',
    'ሹካ', 'ቢላ', 'መቁረጪያዎች', 'ሰርቪሶች', 'መከትከቻ', 'ሳህኖች', 'ምጣድ', 'ስቶቭ', 'ባልዲዎች', 'ማቡኪያ', 'መቀላቀያ', 
    'ይጨምቃል', 'ምንጣፍ', 'ማስወገጃ', 'ቶንዶስ', 'ሰዓት', 'ፓምፕ', 'ፖፖ', 'ሽቦ', 'ብርጭቆ', 'ፌርሙዝ', 'ሳህኖች',
    'መቀነሻ', 'ሳጥኖች', 'ሸራ', 'ስቶቭ', 'ሚዛን', 'ማሽን', 'መለማመጃ' 
]

# List of I-LOC items
i_loc_items = ['መገናኛ', 'ዘፍመሽ', 'ግራንድ', 'ሞል', '3ኛ ፎቅ', '376']

# List of B-LOC items
b_loc_items = ['አዲስ አበባ']

def label_message_utf8_with_birr(message):
    tokens = re.findall(r'\S+', message)  # Tokenize while considering non-ASCII characters
    labeled_tokens = []
    previous_tokens = []

    for i, token in enumerate(tokens):
        # Skip unnecessary tokens
        if token in ['.', '/', './']:
            continue

        # Check if token is a price (e.g., 500 ETB, $100, or ብር)
        if re.match(r'^\d{10,}$', token):
            labeled_tokens.append(f"{token} O")  # Label as O for "other" or outside of any entity
        elif re.match(r'^\d+(\.\d{1,2})?$', token):
            # Check if the next token is "ብር", "ETB", or "etb" to label as B-PRICE
            if i + 1 < len(tokens) and tokens[i + 1] in ['ብር', 'ETB', 'etb']:
                labeled_tokens.append(f"{token} B-PRICE")
            else:
                labeled_tokens.append(f"{token} O")
        elif token in ['ብር', 'ETB', 'etb']:
            labeled_tokens.append(f"{token} I-PRICE")
            # Check if the previous token is a number to label as B-PRICE
            if i > 0 and re.match(r'^\d+(\.\d{1,2})?$', tokens[i - 1]):
                labeled_tokens[-2] = f"{tokens[i - 1]} B-PRICE"
        # Check if token is in the B-PRODUCT list
        elif token in b_product_items:
            # Label the previous two tokens as I-PRODUCT if they exist
            if len(previous_tokens) >= 2:
                labeled_tokens[-2] = f"{previous_tokens[-2]} I-PRODUCT"
                labeled_tokens[-1] = f"{previous_tokens[-1]} I-PRODUCT"
            elif len(previous_tokens) == 1:
                labeled_tokens[-1] = f"{previous_tokens[-1]} I-PRODUCT"
            labeled_tokens.append(f"{token} B-PRODUCT")
        # Check if token is in the I-LOC list
        elif token in i_loc_items:
            labeled_tokens.append(f"{token} I-LOC")
        # Check if token is in the B-LOC list
        elif token in b_loc_items:
            labeled_tokens.append(f"{token} B-LOC")
        # Assume other tokens are part of a product name (this can be refined)
        else:
            labeled_tokens.append(f"{token} O")

        # Keep track of the previous tokens
        previous_tokens.append(token)
        if len(previous_tokens) > 2:
            previous_tokens.pop(0)

    return "\n".join(labeled_tokens)
