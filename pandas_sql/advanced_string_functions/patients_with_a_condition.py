# /*
# Table: Patients
#
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | patient_id   | int     |
# | patient_name | varchar |
# | conditions   | varchar |
# +--------------+---------+
# patient_id is the primary key (column with unique values) for this table.
# 'conditions' contains 0 or more code separated by spaces.
# This table contains information of the patients in the hospital.
#
#
# Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.
#
# Return the result table in any order.
#
# The result format is in the following example.
#
#
#
# Example 1:
#
# Input:
# Patients table:
# +------------+--------------+--------------+
# | patient_id | patient_name | conditions   |
# +------------+--------------+--------------+
# | 1          | Daniel       | YFEV COUGH   |
# | 2          | Alice        |              |
# | 3          | Bob          | DIAB100 MYOP |
# | 4          | George       | ACNE DIAB100 |
# | 5          | Alain        | DIAB201      |
# +------------+--------------+--------------+
# Output:
# +------------+--------------+--------------+
# | patient_id | patient_name | conditions   |
# +------------+--------------+--------------+
# | 3          | Bob          | DIAB100 MYOP |
# | 4          | George       | ACNE DIAB100 |
# +------------+--------------+--------------+
# Explanation: Bob and George both have a condition that starts with DIAB1.
# */
# WITH Patients AS (
#     SELECT 1 AS patient_id, 'Daniel' AS patient_name, 'YFEV COUGH' AS conditions
#     UNION ALL
#     SELECT 2, 'Alice', ''
#     UNION ALL
#     SELECT 3, 'Bob', 'DIAB100 MYOP'
#     UNION ALL
#     SELECT 4, 'George', 'ACNE DIAB100'
#     UNION ALL
#     SELECT 5, 'Alain', 'DIAB201'
# )
# SELECT * FROM Patients where conditions like r'%DIAB100' OR conditions like r'DIAB100%';
import pandas as pd

# Sample data as defined in the SQL query
patients_data = {
    'patient_id': [1, 2, 3, 4, 5],
    'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
    'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201']
}

# Create pandas DataFrame from the sample data
patients_df = pd.DataFrame(patients_data)

# Filter patients with conditions starting with 'DIAB1'
filtered_df = patients_df[patients_df['conditions'].str.contains(r'\bDIAB1', regex=True, na=False)]

# Prepare final result DataFrame
result_df = filtered_df[['patient_id', 'patient_name', 'conditions']].reset_index(drop=True)

# Display the result
print(result_df)
