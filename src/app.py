from datetime import date
from tabulate import tabulate
import click
import JsonManager

@click.group()
def cli():
    pass

#List
@cli.command()
def list():
    data = JsonManager.read_json()
    if len(data) <= 0:
        print('There are not expenses')
    else:
        table_data = []
        table_data.append(['ID', 'Date', 'Description', 'Amount'])
        for exp in data:
            aux = [exp['id'], exp['date'], exp['description'], exp['amount']]
            table_data.append(aux)
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

# Add an expense
@cli.command()
@click.option('--description', type=str, required=True, help='Description of your expense')
@click.option('--amount', type=int, required=True, help='Amount of your expense')
def add(description, amount):
    if amount < 0: 
        print('Invalid amount')
    else:
        data = JsonManager.read_json()
        newID = len(data)+1
        new_entry = {'id': newID, 'date': date.today().strftime("%d-%m-%Y"), 'description': description, 'amount': amount}
        data.append(new_entry)
        JsonManager.write_json(data)
        print(f'Expense added successfully (ID: {newID})')

#Summary
@cli.command()
def summary():
    total = 0
    data = JsonManager.read_json()
    for exp in data:
        total += exp['amount']
    print(f'Total expenses: ${total}')    

if __name__ == '__main__':
    cli()