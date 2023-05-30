# importing module
from pandas import *
import math

min_samples = 1

# Reads in CSV and processes it slightly
def read(file, cumulative):

    data = read_csv(file)
    data.fillna(0, inplace=True)

    if cumulative== True:
        data = make_df_cumulative(data)

    return data

# This function takes a CSV and feeds its columns into get_bias
# Separated by age
def calculate_columns(data):

    max_age = 10
    age_counter = 0
    bias_array = []
    type_array = []
    token_array = []
    overlap_array = []

    while age_counter <max_age + 1:
        null_name = str(age_counter) + "null"
        overt_name = str(age_counter) + "overt"

        null_col = data[null_name].tolist()
        overt_col = data[overt_name].tolist()

        bias, type_count, token = get_bias(null_col, overt_col)
        overlap = get_overlap(null_col, overt_col)

        bias_array.append(bias)
        type_array.append(type_count)
        token_array.append(token)
        overlap_array.append(overlap)

        age_counter += 1
    
    return bias_array, type_array, token_array, overlap_array

# This function finds the empirical overlap between two forms.
def get_overlap(col1, col2):
    min_sample = 1
    type_counter = 0
    overlap_counter = 0

    if len(col1) == len(col2):
        col_height = len(col1)

        for a in range(col_height):
            if float(col1[a]) + float(col2[a]) >= min_sample:
                type_counter += 1

                if float(col1[a]) > 0 and float(col2[a]) > 0:
                    overlap_counter += 1

    if type_counter == 0:
        overlap_ratio = 0
    else:
        overlap_ratio = overlap_counter/type_counter

    return overlap_ratio

# This function adds up the favored form in each row between the two columns,
# Then divides that by the total tokens
def get_bias(col1, col2):
    total_tokens = 0
    total_fav = 0
    min_sample = 1
    type_counter = 0

    if len(col1) == len(col2):
        col_height = len(col1)

        for a in range(col_height):

            #if a == 0:
            #    # This skips "say"
            #    continue
            if float(col1[a]) + float(col2[a]) >= min_sample:
                type_counter += 1
                total_tokens = total_tokens + float(col1[a]) + float(col2[a])
                total_fav = total_fav + max(float(col1[a]), float(col2[a]))
        
        if total_tokens >0:
            bias = round(total_fav/total_tokens,2)
        else:
            bias = 0

        return bias, type_counter, total_tokens

    else:
        print("Columns are not the same size")
        return "n/a", "n/a", "n/a"

# Makes the df counts cumulative across age   
def make_df_cumulative(data):

    age_counter = 1
    null_cumulative = data["0null"]
    overt_cumulative = data["0overt"]

    while age_counter < 11:

        null_name = str(age_counter) + "null"
        overt_name = str(age_counter) + "overt"

        null_cumulative = data[null_name] + null_cumulative
        data[null_name] = null_cumulative

        overt_cumulative = data[overt_name] + overt_cumulative
        data[overt_name] = overt_cumulative

        age_counter += 1

    return data

# Calculates the expected overlap between determiners (or complementizers in this case)
def expected_value(B, N, S):

    if N == 0:
        return 0
    
    harm_n = 0
    # Get probability using Zipf's Law
    for i in range(N):
        # Harmonic series until N-- checked that this is good
        harm_n += 1/(i+1)

    expected_sum = 0
    for r in range(N):
        
        # Probability of noun r occuring a corpus of N word types
        p_r = 1/((r+1)*harm_n)
        #print(p_r)

        #print(S*1/((r+1)*h_n))

        # Simulate S iterations of the verb with determiner combinations to get expected amount of overlap for this verb
        # Second term- prob that verb is not sampled during S trials, Third term- prob that verb is exclusively with ith determiner.
        # E_r = chance that there will be overlap for rth verb 
        E_r = 1 - math.pow((1-p_r),S)- (math.pow((B*p_r + 1 - p_r),S)- math.pow((1-p_r),S))- (math.pow(((1-B)*p_r + 1 - p_r),S)- math.pow((1-p_r),S))
        #print(math.pow(B*p_r + 1 - p_r,S))
        #print(E_r)
        expected_sum += E_r
    # Average across different verbs
    expected_val = expected_sum/N

    

    return expected_val

# The whole process, performed and written to a csv file
def csv_to_bias(file):
    if "dir" in file:
        df = read(file, True)
    else:
        df = read(file, False)
    bias_array, type_array, token_array, overlap_array = calculate_columns(df)

    pred_array = []
    for i in range(len(bias_array)):
        pred_array.append(expected_value(bias_array[i], type_array[i], token_array[i]))

    filename = file[0:-4] + "_2predictions.csv"

    with open(filename,"w") as outfile:

            ## Write the first line of the csv so we know what we're looking at
            first_line = "age, bias, N, S, pred, empirical\n"
            
            outfile.write(first_line)

            for age in range(len(bias_array)):
                next_line = str(age)+ "," + str(bias_array[age]) + "," + str(type_array[age]) + "," + str(token_array[age]) + "," + str(pred_array[age]) + "," + str(overlap_array[age])+ "\n"
                outfile.write(next_line)

    return bias_array, type_array, token_array, pred_array

# Testing bias
#the_val = [5,30,20,5]
#a_val = [20,10,10,0]
#print(get_bias(the_val, a_val))

file_list = ["english_child.csv", "english_child_dir.csv", "spanish_child.csv", "spanish_child_dir.csv"]
for file in file_list:
    bias_array, type_array, token_array, pred_array = csv_to_bias(file)

#expected_array = []
#for i in range(len(bias_array)):
#    expected_array.append(expected_value(bias_array[i], type_array[i], token_array[i]))

#print(expected_array)

#print(expected_value(0.826, 363, 1472))



