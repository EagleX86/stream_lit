import streamlit as st

def main():
    st.title("Travel Planning App")

    st.sidebar.header("Travel Parameters")

    # Input parameters
    days = st.sidebar.number_input("Number of days", min_value=1, max_value=30, value=7)
    budget = st.sidebar.number_input("Total budget ($)", min_value=100, value=1000)
    hotel_rent_per_night = st.sidebar.number_input("Hotel rent per night ($)", min_value=50, value=100)
    daily_expense = st.sidebar.number_input("Daily expenses ($)", min_value=0, value=50)

    st.sidebar.markdown("### Travel Plan")

    # Calculate budget details
    total_hotel_cost = hotel_rent_per_night * days
    total_daily_expenses = daily_expense * days
    total_cost = total_hotel_cost + total_daily_expenses
    remaining_budget = budget - total_cost

    # Display results
    st.write(f"**Number of days**: {days}")
    st.write(f"**Total budget**: ${budget}")
    st.write(f"**Hotel rent per night**: ${hotel_rent_per_night}")
    st.write(f"**Daily expenses**: ${daily_expense}")

    st.write(f"**Total hotel cost**: ${total_hotel_cost}")
    st.write(f"**Total daily expenses**: ${total_daily_expenses}")
    st.write(f"**Total estimated cost**: ${total_cost}")

    if remaining_budget >= 0:
        st.success(f"Your travel plan is within budget! You have ${remaining_budget} remaining.")
    else:
        st.error(f"Your travel plan exceeds the budget by ${-remaining_budget}. Consider adjusting your parameters.")

if __name__ == "__main__":
    main()
