from datetime import date, datetime
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

#Delete
@cli.command()
@click.option('--id', type=int, required=True)
def delete(id):
    data = JsonManager.read_json()
    item = next((i for i in data if i['id'] == id), None)
    if not item:
        print('Expense not found')
    else:
        data.remove(item)
        JsonManager.write_json(data)
        print('Expense deleted')

#Update
@cli.command()
@click.option('--id', type=int, required=True)
@click.option('--description', type=str, required=False)
@click.option('--amount', type=int, required=False)
def update(id, description, amount):
    data = JsonManager.read_json()
    if amount < 0: print('Invalid amount')
    item = next((i for i in data if i['id'] == id), None)
    if not item:
        print(f'Expense with ID {item['id']} not found')
    else:
        if description != "":
            item['description'] = description
        if amount is not None:
            item['amount'] = amount
        JsonManager.write_json(data)
        print(f'Expense with ID {item['id']} updated')

@cli.command()
@click.option('--month', type=int, required=True)
def summary_by_month(month):
    month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    if month<1 or month>12: print('Invalid month')
    data = JsonManager.read_json()
    total = 0
    for exp in data:
        date_aux = datetime.strptime(exp['date'], "%d-%m-%Y")
        m = date_aux.month
        if m == month:
            total += exp['amount']
    print(f'Total expenses for {month_list[month-1]}: ${total}')

if __name__ == '__main__':
    cli()