# Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

# Complete the function get_issuer() that will use the values shown below to determine the card issuer for a given card number. If the number cannot be matched then the function should return the string Unknown.

# | Card Type  | Begins With          | Number Length |
# |------------|----------------------|---------------|
# | AMEX       | 34 or 37             | 15            |
# | Discover   | 6011                 | 16            |
# | Mastercard | 51, 52, 53, 54 or 55 | 16            |
# | VISA       | 4                    | 13 or 16      |
# Examples
# get_issuer(4111111111111111) == "VISA"
# get_issuer(4111111111111) == "VISA"
# get_issuer(4012888888881881) == "VISA"
# get_issuer(378282246310005) == "AMEX"
# get_issuer(6011111111111117) == "Discover"
# get_issuer(5105105105105100) == "Mastercard"
# get_issuer(5105105105105106) == "Mastercard"
# get_issuer(9111111111111111) == "Unknown"

def get_issuer(card_number):
    match len(str(card_number)):
        case 15:
            if str(card_number)[0:2] == "34" or str(card_number)[0:2] == "37":
                return "AMEX"
        case 13:
            if str(card_number)[0] == "4":
                return "VISA"
        case 16:
            if str(card_number)[0:2] in ["51","52","53","54","55"]:
                return "Mastercard"
            if str(card_number)[0] == "4":
                return "VISA"
            if str(card_number)[0:4] == "6011":
                return "Discover"
    return "Unknown"
        
print(get_issuer(41111111111111))
