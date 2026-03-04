import json

with open("universities.json") as f:
    universities = json.load(f)

def recommend_universities(region, interest):

    results = []

    for uni in universities:

        # handle region whether string or list
        uni_region = uni["region"]

        if isinstance(uni_region, list):
            uni_region = uni_region[0]

        uni_region = uni_region.lower()

        uni_strengths = [s.lower() for s in uni["strengths"]]

        if region.lower() == uni_region and interest.lower() in uni_strengths:
            results.append(uni["name"])

    return results

def compare_universities(index1, index2):

    uni1 = universities[index1]
    uni2 = universities[index2]

    print("\n===== UNIVERSITY COMPARISON =====")

    print("\nUniversity 1:", uni1["name"])
    print("City:", uni1["city"])
    print("Tuition Fee:", uni1["tuition_fee"])
    print("Living Cost:", uni1["estimated_living_cost_per_month"])
    print("Strengths:", ", ".join(uni1["strengths"]))
    print("\n--------------------------------")
    print("\nUniversity 2:", uni2["name"])
    print("City:", uni2["city"])
    print("Tuition Fee:", uni2["tuition_fee"])
    print("Living Cost:", uni2["estimated_living_cost_per_month"])
    print("Strengths:", ", ".join(uni2["strengths"]))
    
def estimate_cost(index):

    uni = universities[index]

    tuition = uni["tuition_fee"]

    living_cost = uni["estimated_living_cost_per_month"]

    months = 5   # typical SAP semester

    total_cost = tuition + (living_cost * months)

    print("\n===== SAP COST ESTIMATE =====")

    print("University:", uni["name"])
    print("City:", uni["city"])
    print("Tuition Fee:", tuition)
    print("Living Cost per Month:", living_cost)

    print("\nEstimated Living Cost for 5 months:", living_cost * months)

    print("\nEstimated Total SAP Cost:", total_cost)

def chatbot():

    print("Welcome to SRM SAP Assistant !!")
    print("How can I help you?")
    
    while True:

        print("\nChoose an option:")
        print("1. View all universities")
        print("2. Find best university for me")
        print("3. SAP Program details")
        print("4. Compare Universities")
        print("5. Estimate Cost of Living")
        print("6. Contact SAP Coordinator")
        print("7. Mail your doubts to SAP Team")
        print("8. Exit")

        choice = input("Enter option number: ")

        if choice == "1":
            for uni in universities:
                 print("-", uni["name"])

        elif choice == "2":

            print("\nLet's find the best university for you!")

            print("\nSelect preferred region:")
            print("1 North America")
            print("2 Europe")
            print("3 Asia")

            region_choice = input("Enter option: ")

            if region_choice == "1":
                region = "North America"

            elif region_choice == "2":
                region = "Europe"

            elif region_choice == "3":
                region = "Asia"

            else:
                print("Invalid option")
                continue

            print("\nSelect your interest:")
            print("1 AI / Computer Science")
            print("2 Engineering")
            print("3 Business")
            print("4 Biotechnology")

            interest_choice = input("Enter option: ")

            if interest_choice == "1":
                interest = "AI"

            elif interest_choice == "2":
                interest = "Engineering"

            elif interest_choice == "3":
                interest = "Business"

            elif interest_choice == "4":
                interest = "Biotechnology"

            else:
                print("Invalid option")
                continue

            recommendations = recommend_universities(region, interest)

            print("\nRecommended universities for you:")

            if len(recommendations) == 0:
                print("No matches found.")

            else:
                for uni in recommendations:
                    print("-", uni)

        elif choice == "3":
                print("\nThe Semester Abroad Program (SAP) allows students to spend one full semester at a partner university overseas. 📋 Key Facts: • Duration: 1 semester (4–6 months) • Credits: Fully transferable • Universities: 6+ partner institutions • Available to: Year 2 & 3 students (min. GPA 3.0) • Scholarships: Available for eligible students 📅 Application Timeline: • Nominations: Jan–Feb • Applications: Feb–Apr • Decisions: May • Departure: Aug/Sep 💡 Pro Tip: Apply early — spots fill fast!")

        elif choice == "4":

                print("\nChoose two universities to compare:\n")

                for i, uni in enumerate(universities):
                    print(i + 1, "-", uni["name"])

                try:
                    num1 = int(input("\nEnter first university number: ")) - 1
                    num2 = int(input("Enter second university number: ")) - 1

                    if num1 < 0 or num2 < 0:
                        print("Invalid selection")
                        continue

                    compare_universities(num1, num2)

                except:
                    print("Please enter valid numbers.")

        elif choice == "5":

                print("\nSelect a university to estimate cost:\n")

                for i, uni in enumerate(universities):
                    print(i + 1, "-", uni["name"])

                try:
                    num = int(input("\nEnter university number: ")) - 1

                    if num < 0 or num >= len(universities):
                        print("Invalid selection")
                        continue

                    estimate_cost(num)

                except:
                    print("Please enter a valid number.")
        
        elif choice == "6":
                print("\n choose department:")
                print("1. CTech")
                print("2. Cintel")
                print("3. others")
                dept = input("Enter option: ")
                if dept == "1":
                    print("\nContact CTech SAP Coordinator:")
                    print("Name: Dr. Alice")
                    print("Email: alice.ctech@srmist.edu.in")
                elif dept == "2":
                    print("\nContact Cintel SAP Coordinator:")
                    print("Name: Dr. Anitha")
                    print("Email: anitha.cintel@srmist.edu.in")
                elif dept == "3":
                    print("\nContact General SAP Coordinator:")
                    print("Name: Dr. Kumar")
                    print("Email: kumar@srmist.edu.in")

        elif choice == "7":
                print("\nMail your doubts to SAP Team:")
                print("Email: IRsrmktr@srmist.edu.in")

        elif choice == "8":               
              print("\nThank you for using SRM SAP Assistant. Goodbye!")
              break
        
        else:
                print("\nInvalid option. Try again.")


chatbot()