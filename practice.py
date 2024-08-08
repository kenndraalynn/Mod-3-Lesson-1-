service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

while True:
    ticketname = input("What is your first name? ")
    issueout = input("Please list the problem ")

    helpedyet = input("Has your problem been solved yet? Yes or No ").lower()

    if helpedyet == "yes":
        openclosed = "closed"
    elif helpedyet == "no":
        openclosed = "open"
    else: 
        openclosed = False
        print("Invalid input")
        continue

    if openclosed != False:
        service_tickets["Ticket005"] = {"Customer": ticketname, "Issue": issueout, "Status": openclosed}
        print(service_tickets)
        break
    else:
        print("Try again.")