service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket(ticket_name, issue, status):
    ticket_id = f"Ticket{len(service_tickets) + 1:03d}"
    service_tickets[ticket_id] = {"Customer": ticket_name, "Issue": issue, "Status": status}

def main():
    while True:
        ticketname = input("What is your first name? ")
        issueout = input("Please list the problem: ")

        helpedyet = input("Has your problem been solved yet? Yes or No: ").lower()

        if helpedyet == "yes":
            openclosed = "closed"
        elif helpedyet == "no":
            openclosed = "open"
        else: 
            print("Invalid input. Please enter 'Yes' or 'No'.")
            continue

        add_ticket(ticketname, issueout, openclosed)
        print(service_tickets)

        another = input("Would you like to add another ticket? Yes or No: ").lower()
        if another != "yes":
            break

if __name__ == "__main__":
    main()