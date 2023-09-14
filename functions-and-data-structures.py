#Reuable Function Example, Adding Tax
#Unstructured Function
bill = 150.00
tax_rate = 15
total_tax = (bill * tax_rate) / 100.00
print ('Total Tax: ', total_tax)

#Structured Function
def calculate_bill (bill, tax_rate):
  return (bill * tax_rate) /100.00

#Note: Functions only run when they are called.
print ('Total Tax: ',calculate_bill(250,15))

#### ####

#Local and Global Variables
global_var= 10

def fn1 ():
  local_var = 20
  print('Global Var: ', global_var, 'Local Var: ', local_var)

#Reminder: Functions only run when they are called.
fn1()

#### ####

