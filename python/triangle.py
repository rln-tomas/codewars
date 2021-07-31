def triangle(row):
	if len(row) == 1: 
		return row
	letters = 'RGB'

	tuples = [m+n for (m,n) in zip(row, row[1:])]
	nextRow = ''
	for t in tuples: 
		nextRow += t[0] if t[0] == t[1] else letters.replace(t[0],'').replace(t[1],'')		
	return triangle(nextRow)
