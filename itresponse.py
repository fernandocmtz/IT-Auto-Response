import datetime

def generate_ticket_id(initials):
    """Generate a unique ticket ID using initials and the current date."""
    today = datetime.datetime.now()
    formatted_date = today.strftime("%m%d%y")
    return f"{initials.upper()}{formatted_date}"

def password_reset_case(is_registered, ticket_id):
    """Generate the description and resolution for a password reset case."""
    if is_registered:
        description = "The client is requesting a password reset and is already registered on MyPassword."
        resolution = (f"{ticket_id}: Client is already registered on the MyPassword Assistance. Guide the client on the process to change the password on 'Reset Password'.")
    else:
        description = "The client is requesting a password reset and is not registered on MyPassword."
        resolution = (f"{ticket_id}: Verified client information. Added phone number and personal email as MyPassword sign-in methods. "
                      "Provided the MyPassword information to change the password under 'Forgot My Password' > 'Reset Password'.")
    return description, resolution

def expired_password_case(ticket_id, expiry_date):
    """Generate the description and resolution for an expired password case."""
    description = f"The client is requesting a password reset because the password expired on {expiry_date}."
    resolution = (f"{ticket_id}: Verified client information. Added phone number and personal email as MyPassword sign-in methods. "
                  f"Informed the client that their password expired on {expiry_date}. Provided the MyPassword information to change the password under 'Forgot My Password' > 'Reset Password'.")
    return description, resolution

def password_reset_email_case(ticket_id, email_date, email_time):
    """Generate the description and resolution for a password reset email case."""
    description = f"Client sent an email on {email_date} at {email_time} requesting support with a password reset."
    resolution = f"{ticket_id}: Client receives our auto-response email with further instructions."
    return description, resolution

def disabled_account_case(is_in_student_ou, last_semester, ticket_id):
    """Generate the description and resolution for a disabled account case."""
    description = (f"The client is requesting support for a disabled account. The account is "
                   f"{'in the student OU' if is_in_student_ou else 'not in the student OU'}. "
                   f"The last semester the client attended was {last_semester}.")
    if is_in_student_ou:
        resolution = (f"{ticket_id}: Verified client information. Re-enabled account. Assisted client in resetting password online. "
                      "Verified client could sign in. Registered the two sign-in methods on the MyPassword Assistant.")
    else:
        resolution = (f"{ticket_id}: Verified client information. Moved account to AD. Re-enabled account. Assisted client in resetting password online. "
                      "Verified client could sign in. Provided the MyPassword website information to change the password under 'Forgot password' > 'Manage account'.")
    return description, resolution

def authentication_error_case(ticket_id):
    """Generate the description and resolution for an authentication error case."""
    description = "The client called to report that they are encountering an 'CAS Validation Failed' error when attempting to sign in to Jagnet."
    resolution = (f"{ticket_id}: Verified client's information. Let the Client know that Jagnet only works with the username, not the full email account. "
                  "The client was able to log in.")
    return description, resolution

def wifi_connection_case(ticket_id):
    """Generate the description and resolution for a WiFi connection issue."""
    description = "The client is unable to connect to the WiFi and requested assistance."
    resolution = (f"{ticket_id}: Provided the options to select and was able to connect successfully. "
                  "EAP: PEAP, Phase 2: MSCHAPV2, CA certificate: use system, Online Certificate: Do not Validate, "
                  "Domain: southtexascollege.edu, Identity: your username, Anonymous Identity: leave blank, password: your password.")
    return description, resolution

def transcript_support_case(ticket_id):
    """Generate the description and resolution for transcript support."""
    description = "The client is requesting access to an unofficial transcript but has not been a student for a long time."
    resolution = (f"{ticket_id}: Informed the client that access cannot be provided. Provided details on how to request a transcript online or directly at the college.")
    return description, resolution

def chat_password_reset_case(ticket_id):
    """Generate the description and resolution for a Chat Password Reset case."""
    chat_time = input("Enter the time when the client submitted the chat (HH:MM AM/PM): ").strip()
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

        if ticket_type == "1":
            is_registered = input("Is the client registered on MyPassword? (yes/no): ").strip().lower() == "yes"
            description, resolution = password_reset_case(is_registered, ticket_id)
        elif ticket_type == "2":
            expiry_date = input("Enter the date when the password expired (MM/DD/YY): ")
            description, resolution = expired_password_case(ticket_id, expiry_date)
        elif ticket_type == "3":
            email_date = input("Enter the date of the email (MM/DD/YY): ")
            email_time = input("Enter the time of the email (HH:MM): ")
            description, resolution = password_reset_email_case(ticket_id, email_date, email_time)
        elif ticket_type == "4":
            is_in_student_ou = input("Is the account in the student OU? (yes/no): ").strip().lower() == "yes"
            last_semester = input("What was the last semester the client attended? (e.g., Spring 2023, Fall 2024): ")
            description, resolution = disabled_account_case(is_in_student_ou, last_semester, ticket_id)
        elif ticket_type == "5":
            description, resolution = authentication_error_case(ticket_id)
        elif ticket_type == "6":
            description, resolution = wifi_connection_case(ticket_id)
        elif ticket_type == "7":
            description, resolution = transcript_support_case(ticket_id)
        elif ticket_type == "8":
            description, resolution, internal_notes = chat_password_reset_case(ticket_id)
        elif ticket_type == "9":
            print("\nExiting IT & Support Auto Response System. Goodbye!")
            break
        else:
            print("Invalid ticket type selected. Please try again.")
            continue

        print("\n📌 **Generated Ticket**")
        print("-" * 50)
        print(f"🔹 **Ticket ID:** {ticket_id}\n")
        print(f"🔹 **Description:**\n{description}\n")
        print(f"🔹 **Resolution:**\n{resolution}\n")
        print("🔹 **Status:** Resolved ✅")
        print("-" * 50)

if __name__ == "__main__":
    main()
