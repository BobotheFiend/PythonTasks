#displays the population census  


print("""

                 Welocome to the American population Census!!!

         The following years contain a population census for each year! 

                       "2027" "2028" "2029" "2030" "2031"

        """);
        
population = 312032486;
birth_rate = 31536000/7;
death_rate = 31536000/13;
immigration_rate = 31536000/45;
total = int((birth_rate-death_rate)+immigration_rate);

years = int(input("to view the population, select a year, 2027, 2028, 2029, 2030, 2031 : "))
match(years):
    case 2027 : 
        first_year = population+total
        print(f"The current population in the year 2027 is {first_year}")
    case 2028 : 
        second_year = first_year+total
        print(f"The current population in the year 2027 is {second_year}")
    case 2029 : 
        third_year = second_year+total
        print(f"The current population in the year 2027 is {third_year}")
    case 2030 : 
        fourth_year = third_year+total
        print(f"The current population in the year 2027 is {fourth_year}")
    case 2031 : 
        fifth_year = fourth_year+total
        print(f"The current population in the year 2027 is {fifth_year}")
    case _ : 
        print("Invalid input")
