import streamlit as st
from datetime import datetime
import smtplib
from email.message import EmailMessage

# Constants
HOTEL_NAME = "Gurukripa"
HOTEL_ADDRESS = "Tehsil Chauraha, Shujalpur Mandi, Madhya Pradesh"
HOTEL_CONTACT = "9669609673"
HOTEL_EMAIL = "gurukripa5896@gmail.com"  # Replace with actual hotel email
PASS = "uhlp kqck dzyf wgxp"
MY_EMAIL = "sparmar5896@gmail.com"

# Helper function to send emails
def send_email(customer_email, booking_details):
    try:
        # Set up email
        msg = EmailMessage()
        msg["Subject"] = f"Booking Confirmation - {HOTEL_NAME}"
        msg["From"] = "{HOTEL_EMAIL}"  # Replace with sender email
        msg["To"] = f"{customer_email}, {MY_EMAIL},{HOTEL_EMAIL}"
        msg.set_content(f"Dear Guest,\n\n{booking_details}")

        # SMTP setup (use a real SMTP server)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(HOTEL_EMAIL, PASS)  # Replace with credentials
            server.send_message(msg)
        st.success("Booking confirmation email sent!")
    except Exception as e:
        st.error(f"Error sending email: {e}")

# App layout
st.set_page_config(page_title=HOTEL_NAME, layout="centered")

# Set up custom CSS for background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.zastavki.com/pictures/1920x1200/2012/Interior_Hotel_Room_033155_.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: red;  # You may change text color as needed for better visibility
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Home Page
st.title(f"Welcome to {HOTEL_NAME} 🌟")
st.subheader(HOTEL_ADDRESS)
st.write(f"Contact us at: {HOTEL_CONTACT}")

#st.image("https://wallpaperaccess.com/full/2690784.jpg", caption="Experience luxury and comfort")  # Replace with actual hotel image

# Calendar for date selection
st.header("Book Your Stay")
col1, col2 = st.columns(2)
with col1:
    check_in = st.date_input("Select Check-in Date", min_value=datetime.now().date())
with col2:
    check_out = st.date_input("Select Check-out Date", min_value=check_in)

# Validate date selection
if check_out <= check_in:
    st.warning("Check-out date must be after check-in date!")
else:
    # Collect guest details
    st.header("Guest Details")
    guest_name = st.text_input("Full Name")
    guest_email = st.text_input("Email Address")
    guest_phone = st.text_input("Phone Number")
    number_of_guests = st.number_input("Number of Guests", min_value=1, step=1)

    # Generate Estimate
    if st.button("Generate Estimate"):
        days_staying = (check_out - check_in).days
        room_rate = 2000  # Example room rate per night
        total_cost = days_staying * room_rate

        # Booking details
        booking_details = f"""
        Hotel Name: {HOTEL_NAME}
        Address: {HOTEL_ADDRESS}
        Contact: {HOTEL_CONTACT}

        Guest Name: {guest_name}
        Email: {guest_email}
        Phone: {guest_phone}

        Check-in: {check_in}
        Check-out: {check_out}
        Number of Guests: {number_of_guests}
        Stay Duration: {days_staying} night(s)
        Total Cost: ₹{total_cost}

        Thank you for choosing {HOTEL_NAME}!
        """
        st.text_area("Booking Summary", booking_details, height=300)
        if guest_email and guest_name:
            send_email(guest_email, booking_details)
        else:
            st.error("Please enter valid guest details.")
