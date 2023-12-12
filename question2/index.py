import pandas as pd

def getVowelsCount(titleStr):
	vowelsCtr = 0
	vowelsStr = 'AaEeIiOoUu'

	for char in str(titleStr):
		if char in vowelsStr:
			vowelsCtr += 1

	return vowelsCtr

csvData = pd.read_csv("titles.csv")
csvData['Vowels'] = csvData.apply(lambda row: getVowelsCount(row['title']), axis=1)
print(csvData.head())
csvData.to_csv("output.csv", index = False)