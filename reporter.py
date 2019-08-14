import papermill as pm

pm.execute_notebook(
   'template.ipynb',
   'sales_feb.ipynb',
   parameters=dict(filename="sales_feb.xlsx")
)