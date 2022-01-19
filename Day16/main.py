from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokeymon Name","Type"]
table.add_row(["picachu","electric"])
table.add_row(["squirtle","water"])
table.add_row(["charmander","fire"])

table.add_column("price",[123,234,234])

table.align = 'l'
print(table)
