import numpy as np

num_of_var = 3
num_of_constrain = 3

# objective function: maximize P = 6x + 5y + 4z
obj = [-6,-5,-4,0]

#constrain:
# 2x+y+z<=180
# x+3y+2z<=300
# 2x+y+2z<=240
constrain = [[2,1,1, 180],[1,3,2,300],[2,1,2,240]]

def generate_tabular(obj, constrain):
    num_of_equations = len(constrain)+1
    mid = np.zeros((num_of_equations,num_of_equations))
    for i in range(mid.shape[0]):
        mid[i,i] = 1
    output = np.zeros((len(constrain)+1, 2*len(constrain[0])))
    for i in range(len(constrain)):
        for j in range(len(constrain[0])-1):
            output[i,j]=constrain[i][j]
        output[i,-1] = constrain[i][-1]
    for i in range(len(obj)-1):
        output[-1,i] = obj[i]
    # output[]
    output[:,len(constrain[0])-1:output.shape[1]-1]=mid
    return output

def simplex_iteration(tabular):
    for k in range(10):
        last_row_min = np.min(tabular[-1, :])
        print(last_row_min)
        if(last_row_min>=0):
            return tabular[-1,-1]
        pivotColumnindex = np.where(tabular[-1,:] == last_row_min)
        pivotColumn = pivotColumnindex[0]
        pivotColumn = pivotColumn[0]
        print("pivotColumn, ", pivotColumn)

        print("min: ", np.min(tabular[0:tabular.shape[0]-1,-1] / tabular[0:tabular.shape[0]-1,pivotColumn]))
        print(tabular[0:tabular.shape[0]-1,-1] / tabular[0:tabular.shape[0]-1,pivotColumn])
        pivotRow = np.where(tabular[0:tabular.shape[0]-1,-1] / tabular[0:tabular.shape[0]-1,pivotColumn] == np.min(tabular[0:tabular.shape[0]-1,-1] / tabular[0:tabular.shape[0]-1,pivotColumn]))
        # print(tabular[-1, pivotColumn])
        pivotRow = pivotRow[0][0]
        pivot = tabular[pivotRow, pivotColumn]
        tabular[pivotRow,:] = tabular[pivotRow,:]/pivot
        for i in range(tabular.shape[0]):
            if i != pivotRow:
                tabular[i,:] = tabular[i,:] - (tabular[i,pivotColumn]*tabular[pivotRow,:])
        print("k:",k)
        print(tabular)

tabular = generate_tabular(obj, constrain)
print(tabular)
print( simplex_iteration(tabular))