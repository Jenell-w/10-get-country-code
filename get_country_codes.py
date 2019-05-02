def get_country_codes(prices):
    codes = []
    code_list = prices.split(", ")
    for item in code_list: 
        country_code = item.split('$')
        codes += country_code[:1]
    return ", ".join(codes)
   
