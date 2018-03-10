csv_string = "'bob','255 summer st','111-123-5555',\n\
                'frank','78 summer st','111-123-5555"

columns = csv_string.split(",")
print(columns[0])
#for item in columns:
#    placeholder = item.replace("\n","")
#    print(placeholder.replace(" ", ''))
