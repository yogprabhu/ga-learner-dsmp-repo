# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
loan_status.plot(kind='bar',title='Loan Status', legend=True)
plt.show()

#Code starts here


# --------------
#Code starts here
# property_and_loan.plot(kind='bar').xlabel('Area')
property_and_loan = data.groupby(by=['Property_Area', 'Loan_Status']).size().unstack()
plt.bar(property_and_loan.index,property_and_loan['Y'])
plt.bar(property_and_loan.index,property_and_loan['N'])
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here
# Q3
education_and_loan=data.groupby(by=['Education', 'Loan_Status']).size().unstack()
plt.bar(education_and_loan.index,education_and_loan['Y'])
plt.bar(education_and_loan.index,education_and_loan['N'])
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()



# --------------
#Code starts here
# Q4
graduate = data[data['Education'] == 'Graduate']
not_graduate=data[data['Education'] == 'Not Graduate']
graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')



#Code ends here

#For automatic legend display
plt.legend()
plt.show()


# --------------
#Code starts here
# Q5
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3, ncols=1)
# plt.scatter(data['ApplicantIncome'],data['LoanAmount'])
data.plot(x='ApplicantIncome',y='LoanAmount', ax=ax_1, kind='scatter', title='Applicant Income')
data.plot(x='CoapplicantIncome',y='LoanAmount', ax=ax_2, kind='scatter', title='Coapplicant Income')
data.plot(x='TotalIncome',y='LoanAmount', ax=ax_3, kind='scatter', title='Total Income')
plt.show()


