
#Setting up database access and connections 
import psycopg2

def main():

    dbase = "FlightData"
    user = "postgres"
    password = "Monkeyonm3!"
    host = "localhost"
    port = 5432
    # curs = None

    try:
        connection = psycopg2.connect(
            dbname=dbase,
            user=user,
            password=password,
            host=host,
            port=port
    )

        curs = connection.cursor()

        curs.execute("SELECT version();")
        version = curs.fetchone()
        print("PostgreSQL db version: ", version)
        
        
        
        opt = False
        while opt == False:

            queries = [
                "Insert Pittsburgh Airport into Origins",
                "Delete Pittsburgh Airport from Origins",
                "Update Origin to set OriginCityName = \"Pittsburgh\" where OriginCityName = \"Pitt\" ",
                "Select * Origin where OriginState = PA",
                "Select Count() of Tail_Number's in FLight_Schedule Table",
                "Select * length and Order By AirTime, Distance both in descending order",
                "Select * from Flight_Schedule and State joined on Tail_Number",
                "Select * Quarter and count() from Period but group by Quarter",
                "Subquery: Select * from Flight_Schedule where delay > 0 in status",
                "Commit Transactions",
                "RollBack"
                ]

        # Construct the prompt message with the options
            prompt_message = "Select an option:\n"
            for i, option in enumerate(queries, start=1):
                prompt_message += f"{i}. {option}\n"

        # Get user input
            choice = input(prompt_message)

        #Check choices and echo choice
            try:
                choice_id = int(choice)
                if 1 <= choice_id <= 11:
                    selection = queries[choice_id - 1]
                    match choice_id: 
                        case 1: 
                            #INSERT
                            curs.execute("Insert into Origin(\"OriginAirportID\", \"OriginAirportSeqID\", \"OriginCityMarketID\",\"OriginCityName\", \"OriginState\", \"OriginStateFips\",\"OriginStateName\") values (19999,1999999,39999,'Pitt','PA',42,'Pennsylvania');")
                            # connection.commit()
                            print("INSERT modifcation noted")
                            
                        case 2: 
                            #DELETE
                            curs.execute("Delete from Origin where \"OriginAirportID\" = 19999;")
                            # connection.commit()
                            print("DELETE modification noted")
                            
                        case 3: 
                            # UPDATE
                            curs.execute("Update Origin set \"OriginCityName\" = 'Pittsburgh' where \"OriginCityName\" = 'Pitt';")
                            print("UPDATE modification noted")
                            
                        case 4: 
                            #Select *
                            curs.execute("Select * from Origin where \"OriginState\" = 'PA'; ")
                            selected = curs.fetchall()
                            for record in selected: 
                                print(record)
                            
                            print("Select * modifcation noted ")
                            
                        case 5: 
                            # COUNT
                            curs.execute("Select COUNT(\"Tail_Number\") as Count from Flight_Schedule;")
                            selected = curs.fetchall()
                            for record in selected: 
                                print(record)
                            print("Select Count shown")
                            
                        case 6: 
                            #Order By
                            curs.execute("Select * from length order by \"AirTime\" desc, \"Distance\" desc;")
                            selected = curs.fetchall()
                            for record in selected: 
                                print(record)
                            print("Sort * shown")
                            
                        case 7: 
                            # Inner JOIN
                            curs.execute("Select * from Flight_Schedule F join Status S on F.\"Tail_Number\" = S.\"Tail_Number\";")
                            selected = curs.fetchall()
                            for record in selected: 
                                print(record)
                            print("Join shown")
                            
                        case 8: 
                            # Grouping
                            curs.execute("Select \"Quarter\", COUNT(*) as period_count from Period group by \"Quarter\";")
                            selected = curs.fetchall()
                            for record in selected: 
                                print(record)
                            print("Grouping By shown")
                            
                        case 9: 
                            # Subquery
                            curs.execute("select * from Flight_Schedule where \"Tail_Number\" in (Select \"Tail_Number\" from Status where \"DepDelay\" > 0);")
                            selected = curs.fetchall()
                            for record in selected: 
                                print(record)
                            print("SubQuery shown")
                        case 10: 
                            # Commit
                            connection.commit()
                            print("Your transactions have been committed.")
                            opt = True
                        case 11: 
                            connection.rollback()
                            print("All unsaved transactions have been rolledback")
                            
                            
                    
                    # print(f"You selected: {selection}")
                    
                    
                else:
                    print("Invalid option. Please select a number between 1 and 11.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        curs.close()
        
    except (Exception, psycopg2.Error) as error:
        print("Error: Couldn't connect to database.", error)
        
    finally:
        if 'connection' in locals() or 'connection' in globals():
            connection.close()
main()          
        