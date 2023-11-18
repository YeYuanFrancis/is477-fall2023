# Assignment 4

- **Inspection ID**: 
Transformed into number format, and edit all inconsistent values to standard format and transformed them into number format as well. 
- **DBA Name and AKA Name**: 
Applied trimming to remove leading and trailing spaces in the 'DBA Name', 'AKA Name'. 
Converted them into title case for consistency. 
Used clustering algorithms to identify and merge variant spellings in the 'DBA Name' and 'AKA Name' columns. 
- **License**:  
Transformed into number format, and edit all inconsistent rows to standard format and transformed them into number format as well.
- **Facility Type**: 
Applied trimming to remove leading and trailing spaces. 
Converted them into title case for consistency.
- **Risk**: 
Applied trimming to remove leading and trailing spaces.
Converted them into title case for consistency.
Used clustering algorithms to identify and merge variant spellings.
Edit two 'Risk 1 (medium)' to 'Risk 2 (medium)' based on the comparision of their violations to others which indicate that other resturants with same violation have Risk 2 (medium). 
- **Address**:
Applied trimming to remove leading and trailing spaces.
Converted them into title case for consistency.
- **City State Zip**: 
Split them into three columns "City", "State", and "Zip" with separator ",". 
- **City**:
Applied trimming to remove leading and trailing spaces.
Converted them into title case for consistency.
Used clustering algorithms to identify and merge variant spellings. especially for "Chicago".
- **State**: 
Applied trimming to remove leading and trailing spaces.
Converted them into upercase for consistency.
- **Zip**:
Transformed into number format, and edit all inconsistent rows to standard format and transformed them into number format as well.
- **Inspection Date**: Adjusted the format of the 'Inspection Date' column to a standard 'YYYY/MM/DD' format. Then, I common tranformed 'Inspection Date' to Date.
- **Inspection Type**:
Applied trimming to remove leading and trailing spaces.
Converted them into title case for consistency.
- **Results**:
Applied trimming to remove leading and trailing spaces.
Converted them into title case for consistency.
- **Violations**:
Splited multi-valued cells with separator "|"




