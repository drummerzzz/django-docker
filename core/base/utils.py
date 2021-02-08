def clean_special_characters(value:str):
  aux = value
  for i in aux:
    if not i.isalpha():
      value = value.replace(i, '')
  return value