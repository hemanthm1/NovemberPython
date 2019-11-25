def assign_grade(score):
    if score > 90:
	    grade = 'A'
	elif score > 80 and score < 90:
	    grade = 'B'
	elif score > 70 and score < 80:
	    grade = 'C'
	elif grade > 60 and score < 70:
	    grade = 'D'
	elif score <= 60:
	    grade = 'F'
	
	return grade
	
	
def day_of_week(dayOfWeek):
    if dayOfWeek == 1:
	    day = 'Monday'
	if dayOfWeek == 2:
	    day = 'Tuesday'
	if dayOfWeek == 3:
	    day = 'Wednesday'
	if dayOfWeek == 4:
	    day = 'Thursday'
	if dayOfWeek == 5:
	    day = 'Friday'
	if dayOfWeek == 6:
	    day = 'Saturday'
	if dayOfWeek == 7:
	    day = 'Sunday'
	
	return day
