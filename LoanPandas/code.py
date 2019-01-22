# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 

# code starts here
bank = pd.read_csv(path) 
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop(columns='Loan_ID')
print(banks.isnull().sum())

bank_mode = banks.mode()
#print(bank_mode)
banks = banks.fillna(0)
print(banks.isna().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(data=banks, index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount', aggfunc=np.mean)



# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed']=='Yes')&(banks['Loan_Status']=='Y')].shape[0]

loan_approved_nse=banks[(banks['Self_Employed']=='No')&(banks['Loan_Status']=='Y')].shape[0]
Loan_Status = 614
percentage_se = (loan_approved_se/Loan_Status)*100
percentage_nse = (loan_approved_nse/Loan_Status)*100
# code ends here


# --------------
# code starts here

banks.Loan_Amount_Term.iloc[0]
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)
banks['Loan_Amount_Term']=banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)

big_loan_term= banks[banks['Loan_Amount_Term']>=25].shape[0]

# code ends here


# --------------
# code starts here
columns_to_show = ['ApplicantIncome', 'Credit_History']
loan_groupby = banks.groupby(by='Loan_Status')
loan_groupby = loan_groupby[columns_to_show]
mean_values = loan_groupby.agg([np.mean])

# code ends here


