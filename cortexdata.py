# given a sparse npz connectome dataset from the Blue Brain Project (https://portal.bluebrain.epfl.ch/downloads/),
# this program converts it into usable data without building the whole matrix
import numpy

# loads file, transfers data into variables
file_name_load = input('what is the file name?')

with numpy.load(file_name_load) as data:
    print(data.files)
    col = data['indices']
    row_ptr = data['indptr']

col_ind = []
for x in range(0, col.shape[0]):
    col_ind.append(x)

# reformats data, transforming it from csc format to a format with presynaptic + postsynapttic neuron lists
row = []
row_count = 0
for x in range(0, len(col_ind)):
    if row_ptr[row_count] == col_ind[x]:
        row_count += 1
        row.append(row_count)
    else:
        row.append(row_count)

print(len(col))
print(len(row))

# Save file
data = numpy.array([col, row])

file_name_save = input("what file name would you like to save the reformatted data to?")
numpy.savez(file_name_save, data)
#1st list is col, 2nd is row