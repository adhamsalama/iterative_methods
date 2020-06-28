import pandas as pd
from jacobi import jacobi
from gauss_seidel import gauss_seidel
from sor import sor


s1 = [4, 3, 0, 24]
s2 = [3, 4, -1, 30]
s3 = [0, -1, 4, -24]

j = jacobi(s1, s2, s3)
g = gauss_seidel(s1, s2, s3)
s = sor(s1, s2, s3, 1.25)

# Write solutions to excel using pandas
with pd.ExcelWriter('solutions.xlsx', mode='w') as writer:  
    pd.DataFrame(j).to_excel(writer, sheet_name='Jacobi')
    pd.DataFrame(g).to_excel(writer, sheet_name='Gauss-Seidel')
    pd.DataFrame(s).to_excel(writer, sheet_name='SOR')
