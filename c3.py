days=500
years= 500//365 #gives the qoutient without decimal
remaining_days= 500%365 
weeks= remaining_days//7
days= years%7 
print("500 days is equal to",years, "year",weeks,"weeks and ",days,"day")