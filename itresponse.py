import datetime

def generate_ticket_id(initials):
    """Generate a unique ticket ID using initials and the current date."""
    today = datetime.datetime.now()
    formatted_date = today.strftime("%m%d%y")
    return f"{initials.upper()}{formatted_date}"

def chat_password_reset_case(ticket_id):
    """Generate the description and resolution for a Chat Password Reset case."""
    chat_time = input("Enter the time when the client submitted the chat (HH:MM AM/PM): ")
    today_date = datetime.datetime.now().strftime("%m/%d/%Y")

    description = f"Client submitted a chat on ask {today_date} at {chat_time} requesting support with a password reset."
    resolution = (f"{ticket_id}: Verified client information. Added phone number and personal email as MyPassword sign-in methods. "
                  "Provided the MyPassword information to change the password under 'Forgot My Password' > 'Reset Password'.")
    
    internal_notes = ("- Ensure the client is providing the correct username (not full email).\n"
                      "- If the client is unable to access MyPassword, confirm security details and advise alternative recovery methods.\n"
                      "- If additional verification is needed, escalate to account services.")

    return description, resolution, internal_notes

def main():
    print("Welcome to IT & Support Auto Response System\n")
    
    # Ask for user initials once and use for all ticket entries
    initials = input("Enter your initials (e.g., FCM): ").upper()

    while True:
        ticket_id = generate_ticket_id(initials)

        print("\nSelect the type of ticket:")
        print("1. Password Reset (General)")
        print("2. Expired Password Reset")
        print("3. Password Reset Email")
        print("4. Disabled Account")
        print("5. Authentication Error")
        print("6. WiFi Connection")
        print("7. Transcript Support")
        print("8. Chat Password Reset")
        print("9. Exit\n")

        ticket_type = input("Enter the ticket type (1-9): ")

        if ticket_type == "8":
            description, resolution, internal_notes = chat_password_reset_case(ticket_id)
        elif ticket_type == "9":
            print("\nExiting IT & Support Auto Response System. Goodbye!")
            break
        else:
            print("Invalid ticket type selected. Please try again.")
            continue  # Restart the loop

        print("\n📌 **Generated Ticket**")
        print("-" * 50)
        print(f"🔹 **Ticket ID:** {ticket_id}\n")
        print(f"🔹 **Description:**\n{description}\n")
        print(f"🔹 **Resolution:**\n{resolution}\n")
        print(f"🔹 **Internal Notes:**\n{internal_notes}\n")
        print("🔹 **Status:** Resolved ✅")
        print("-" * 50)

        # Ask if the user wants to create another request
        another_request = input("\nDo you want to process another request? (yes/no): ").strip().lower()
        if another_request != "yes":
            print("\nExiting IT & Support Auto Response System. Goodbye!")
            break

if __name__ == "__main__":
    main()
