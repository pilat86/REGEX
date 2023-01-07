import re

def is_valid_contact(contact: str) -> bool:
    result = re.fullmatch(r'(([A-Z]{1}[a-z]+(\s){1})+)(\+?)(\s?)((\d(\s*))+(\d{6}))(\:?)(\-?)(\d{4})', contact)
    return result is not None


# Tests:
print(is_valid_contact("Karlik +123 456 789 980312:1234"))  # True
print(is_valid_contact("Los Karlos Lord Antarkticky 999 971224-2846"))  # True
print(is_valid_contact("Policie + 1 5 8 0000000000"))  # True
print(is_valid_contact("Zelva Julie 420 1228 015214:0007"))  # True

print(is_valid_contact("karlik Tucnak T331370n 123456"))  # False
print(is_valid_contact("Tulen +123 123 456:7894"))  # False
print(is_valid_contact("Krajta Python +1456 4567o9.1234"))  # False
print(is_valid_contact("Neznámý Kontakt 0123 9876543210"))  # False