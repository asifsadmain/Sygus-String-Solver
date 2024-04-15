def get_results(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        results = []
        
        for line in lines:
            if (line.startswith("Result: Success")):
                results.append(1)
            elif (line.startswith("Result: Failed")):
                results.append(0)

    return results

dsl_result_1 = get_results("../logs/gpt_dsl_1.log")
dsl_result_2 = get_results("../logs/gpt_dsl_2.log")
dsl_result_3 = get_results("../logs/gpt_dsl_3.log")
dsl_result_4 = get_results("../logs/gpt_dsl_4.log")
dsl_result_5 = get_results("../logs/gpt_dsl_5.log")
dsl_result_6 = get_results("../logs/gpt_dsl_6.log")
dsl_result_7 = get_results("../logs/gpt_dsl_7.log")
dsl_result_8 = get_results("../logs/gpt_dsl_8.log")
dsl_result_9 = get_results("../logs/gpt_dsl_9.log")
dsl_result_10 = get_results("../logs/gpt_dsl_10.log")
dsl_result_11 = get_results("../logs/gpt_dsl_11.log")
dsl_result_12 = get_results("../logs/gpt_dsl_12.log")
dsl_result_13 = get_results("../logs/gpt_dsl_13.log")
dsl_result_14 = get_results("../logs/gpt_dsl_14.log")
dsl_result_15 = get_results("../logs/gpt_dsl_15.log")
dsl_result_16 = get_results("../logs/gpt_dsl_16.log")
dsl_result_17 = get_results("../logs/gpt_dsl_17.log")
dsl_result_18 = get_results("../logs/gpt_dsl_18.log")

python_result_1 = get_results("../logs/gpt_py_1.log")
python_result_2 = get_results("../logs/gpt_py_2.log")
python_result_3 = get_results("../logs/gpt_py_3.log")
python_result_4 = get_results("../logs/gpt_py_4.log")
python_result_5 = get_results("../logs/gpt_py_5.log")
python_result_6 = get_results("../logs/gpt_py_6.log")
python_result_7 = get_results("../logs/gpt_py_7.log")
python_result_8 = get_results("../logs/gpt_py_8.log")
python_result_9 = get_results("../logs/gpt_py_9.log")
python_result_10 = get_results("../logs/gpt_py_10.log")
python_result_11 = get_results("../logs/gpt_py_11.log")
python_result_12 = get_results("../logs/gpt_py_12.log")
python_result_13 = get_results("../logs/gpt_py_13.log")
python_result_14 = get_results("../logs/gpt_py_14.log")
python_result_15 = get_results("../logs/gpt_py_15.log")
python_result_16 = get_results("../logs/gpt_py_16.log")
python_result_17 = get_results("../logs/gpt_py_17.log")
python_result_18 = get_results("../logs/gpt_py_18.log")
python_result_19 = get_results("../logs/gpt_py_19.log")

enc_result_1 = get_results("../logs/gpt_enc_1.log")
enc_result_2 = get_results("../logs/gpt_enc_2.log")
enc_result_3 = get_results("../logs/gpt_enc_3.log")
  
dsl_final_results = [max(x) for x in zip(dsl_result_1, dsl_result_2, dsl_result_3, dsl_result_4, dsl_result_5, dsl_result_6, dsl_result_7, dsl_result_8, dsl_result_9, dsl_result_13, dsl_result_14, dsl_result_15, dsl_result_16, dsl_result_17, dsl_result_18)]
dsl_intersection = [min(x) for x in zip(dsl_result_1, dsl_result_2, dsl_result_3, dsl_result_4, dsl_result_5, dsl_result_6, dsl_result_7, dsl_result_8, dsl_result_9, dsl_result_13, dsl_result_14, dsl_result_15, dsl_result_16, dsl_result_17, dsl_result_18)]
# dsl_final_results = [max(x) for x in zip(dsl_result_16, dsl_result_17, dsl_result_18)]
dsl_failed_tasks = [index+1 for index, value in enumerate(dsl_final_results) if value == 0]

# python_final_results = [max(x) for x in zip(python_result_1, python_result_2, python_result_3, python_result_4, python_result_5, python_result_6, python_result_7, python_result_8, python_result_9, python_result_10, python_result_11, python_result_12, python_result_13, python_result_14, python_result_15, python_result_16, python_result_19, python_result_17, python_result_18)]
python_final_results = [max(x) for x in zip(python_result_13, python_result_14, python_result_15)]
python_failed_tasks = [index+1 for index, value in enumerate(python_final_results) if value == 0]
python_intersection = [min(x) for x in zip(python_result_1, python_result_2, python_result_3, python_result_4, python_result_5, python_result_6, python_result_7, python_result_8, python_result_9, python_result_10, python_result_11, python_result_12, python_result_13, python_result_14, python_result_15)]

enc_final_results = [max(x) for x in zip(enc_result_1, enc_result_2, enc_result_3)]
enc_failed_tasks = [index+1 for index, value in enumerate(enc_final_results) if value == 0]

print("-------------------DSL-------------------") 
print("Total Correct Programs:", dsl_final_results.count(1))
print("Failed Tasks:", dsl_failed_tasks)
print("Intersection:", dsl_intersection.count(1))
print()
print()
print("-------------------Python-------------------")
print("Total Correct Programs:", python_final_results.count(1))
print("Failed Tasks:", python_failed_tasks)
print("Intersection:", python_intersection.count(1))
print()
print()
print("-------------------Encrypted-------------------")
print("Total Correct Programs:", enc_final_results.count(1))
print("Failed Tasks:", enc_failed_tasks)
