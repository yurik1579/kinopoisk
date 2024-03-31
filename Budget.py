import pandas as pd


with open('budget.txt', 'r', encoding='utf-8') as file:
    budget_text = file.read()

print(budget_text)


list_budget1 = budget_text.split('"BUDGET","amount":')
print(list_budget1)
list_budget2 = []
for i in list_budget1:
    budget = i.split(',')[0]
    list_budget2.append(budget)
print(list_budget2)
print(len(list_budget2))

df = pd.read_excel('TOP250.xlsx')
df['Бюджет'] = list_budget2
df.to_excel('TOP250 with budget.xlsx')