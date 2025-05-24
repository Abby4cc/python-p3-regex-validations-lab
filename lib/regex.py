import re

name_regex = re.compile(
    r"^[A-Z][a-z]*(?:[-'][A-Z][a-z]*)*(?: [A-Z][a-z]*(?:[-'][A-Z][a-z]*)*)*$"
)

phone_regex = re.compile(
    r"^(?:\(\d{3}\)\s?\d{3}-\d{4}|\d{10}|\d{3}[-.]\d{3}[-.]\d{4}|(?:\+1\s)?\d{3}\s\d{3}\s\d{4})$"
)

email_regex = re.compile(
    r"^[a-zA-Z][\w\.-]*@[\w\.-]+\.\w{2,}$"
)
