def hostel_chatbot():
    print("🤖 Hello! I am your Hostel Complaint Bot.")
    print("How can I help you today?")
    print("Type 'exit' anytime to end the chat.\n")

    while True:
        complaint = input("You: ").lower()

        if "exit" in complaint:
            print("🤖 Thank you! Your complaints are valuable. Goodbye!")
            break

        elif "food" in complaint:
            print("🤖 Sorry for the inconvenience. We will inform the mess staff about the food issue.")

        elif "room" in complaint or "clean" in complaint or "room clean" in complaint or "room cleaning" in complaint:
            print("🤖 Room cleaning or maintenance request received. Hostel warden will be notified.")

        elif "wifi" in complaint or "internet" in complaint:
            print("🤖 Wifi issues reported. Technician will check it soon.")

        elif "water" in complaint:
            print("🤖 Water problem noted. Maintenance team will resolve it shortly.")

        elif "electricity" in complaint or "light" in complaint:
            print("🤖 Electricity problem noted. We will fix it as soon as possible.")

        else:
            print("🤖 Thank you for your feedback. We will look into the issue.")

# Run the chatbot
hostel_chatbot()