import papermill as pm
import os

# Function to generate report as jupypter notebook and save graph as image file in same directory
def gen_report(template,out_notebook,datafile):
    pm.execute_notebook(template,out_notebook,parameters=dict(filename=datafile))

# Read all data files present in folder "monthly_data" and generate report for all one by one    
try:    
    for filename in os.listdir("monthly_data"):        
        gen_report('template.ipynb',filename.replace('.xlsx','.ipynb'),os.path.abspath('monthly_data\{}'.format(filename)))
except Exception as ex:
    print('Error in generating report, Please check data file and check if report is already generated.')