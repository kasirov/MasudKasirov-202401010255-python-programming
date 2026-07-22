from ticket import create_ticket
from display import display_ticket

def main():
    # 1. Collect ticket data from the user
    ticket_data = create_ticket()
    
    # 2. Check if a ticket was successfully created before displaying
    if ticket_data:
        display_ticket(ticket_data)

if __name__ == "__main__":
    main()