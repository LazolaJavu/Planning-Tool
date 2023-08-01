import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


model_data =  pd.read_excel(r"C:/Users/LazolaJavu/OneDrive - SmartStart/Documents/SmartStart/Ops Department/Mapaseka's Request'/Planning Tool - Coaches/Models/Planning_Model v.01.xlsx", sheet_name="Model")

# Calculate the sum of values based on categories
sum_by_category = model_data.groupby('Franchisor').sum().transpose()

def model():

	with st.expander("More about the Model"):

		st.markdown("""
     - SmartStart operates in multiple Municipalities across south africa. In this page, we show all the active children by Municipalities.
     - How does the figure work:
        - You can select multiple Municipalities to view the active children Performance by that Municipality.
     * [SmartStart Website](https://smartstart.org.za)
    """)

	st.write(model_data)

def franchisor():

	# Get the unique values in the "Franchisor" column
	select_franchisor = model_data["Franchisor"].unique()

	# Create the select box for Franchisor
	select_box1 = st.sidebar.selectbox("Select a Franchisor", select_franchisor)

	# Filter the DataFrame based on the selected Franchisor
	filtered_data = model_data[model_data["Franchisor"] == select_box1]

	# # Get the unique values in the "Full Name" (Coach) column from the filtered data
	# select_coach = filtered_data["Full Name"].unique()

	# # Create the select box for Coach
	# select_box2 = st.sidebar.selectbox("Select a Coach", select_coach)

	# # Filter the DataFrame based on the selected Coach
	# final_data = filtered_data[filtered_data["Full Name"] == select_box2]

	# Add a slider to the sidebar
	Club_Meeting = st.sidebar.slider("Club Meeting (hrs)", min_value=2, max_value=5, value=2, step=1)
	AR = st.sidebar.slider("Annual Reaccreditation (hrs)", min_value=2, max_value=10, value=2, step=1)
	PQA = st.sidebar.slider("PQA (hrs)", min_value=4, max_value=10, value=4, step=2)
	Smartspace = st.sidebar.slider("Due for Smartspace (hrs)", min_value=1.5, max_value=6.0, value=1.5, step=0.5)
	PrePQA = st.sidebar.slider("Planning for PQA (PrePQA) (hrs)", min_value=1.5, max_value=5.0, value=1.5, step=0.5)
	Coaching_Circle = st.sidebar.slider("Coaching Circle (hrs)", min_value=2, max_value=10, value=2, step=1)
	Club_leader_meetings = st.sidebar.slider("Club leader meetings (hrs)", min_value=2, max_value=10, value=2, step=1)
	Porridge = st.sidebar.slider("Porridge", min_value=16, max_value=24, value=16, step=1)
	Coach_Admin_Time  = st.sidebar.slider("Coach Admin Time", min_value=8, max_value=12, value=8, step=1)
	Community_Engagement_for_Matching = st.sidebar.slider("Community Engagement for Matching", min_value=24, max_value=30, value=24, step=1)
	Matching_Day  = st.sidebar.slider("Matching Day", min_value=10, max_value=15, value=10, step=1)
	PreStartup_Planning  = st.sidebar.slider("PreStartup Planning", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
	Startup_Training = st.sidebar.slider("Startup Training", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
	CP_Planning = st.sidebar.slider("CP Planning", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
	BS_Planning = st.sidebar.slider("BS Planning", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
	Consolidation  = st.sidebar.slider("Consolidation", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
	Briefings_Coach_Meetings  = st.sidebar.slider("Briefings Coach Meetings", min_value=4, max_value=8, value=4, step=1)
	Coach_Support_Time = st.sidebar.slider("Coach Support Time", min_value=8, max_value=15, value=8, step=1)


	# st.subheader(f'_Overall Backlog and Summarised work for :blue[{select_box2}]: A detailed SmartStart Coach Plan :purple_heart:_')

	c1, c2 = st.columns(2)

	
	c1.subheader("_July Backlog represented by days to complete._")

	# c1.markdown("Backlog for the Franchisor: See the performance against the backlog and the hours it will take to complete.")
	c2.subheader("_Planning represented by days to complete._")

	col1, col2, col3, col4, col5 = st.columns((1, 1, 1, 1,1))

	# options = ["Coach Plan", "Due on SmartLink", "Franchisor Information", "Training Plan on SmartLink or IP"]

	# # Create a selectbox for choosing the option
	# selected_option = col3.selectbox('Select Data:', options)



	Activity_1 = (col3.number_input('Enter your Club Meetings Planned', min_value=0, max_value=100, step=1)*Club_Meeting)/8
	Activity_2 = (col3.number_input('Enter your AR Planned', min_value=0, max_value=100, step=1)*AR)/8
	Activity_3 = (col3.number_input('Enter your PQA Planned', min_value=0, max_value=100, step=1)*PQA)/8
	Activity_4 = (col3.number_input('Enter your Smartspace Planned', min_value=0, max_value=100, step=1)*Smartspace)/8
	Activity_5 = (col3.number_input('Enter your PrePQA Planned', min_value=0, max_value=100, step=1)*PrePQA)/8
	Activity_6 = (col3.number_input('Enter your Coaching Circle Planned', min_value=0, max_value=100, step=1)*Coaching_Circle)/8
	Activity_7 = (col3.number_input('Enter your Club leader meetings Planned', min_value=0, max_value=100, step=1)*Club_leader_meetings)/8
	Activity_8 = (col3.number_input('Enter your Porridge Planned', min_value=0, max_value=100, step=1)*Porridge)/8
	Activity_9 = (col3.number_input('Coach Admin Time', min_value=0, max_value=100, step=1)*Coach_Admin_Time)/8
	Activity_11 = (col4.number_input('Enter your Matching Day Planned', min_value=0, max_value=100, step=1)*Matching_Day)/8
	Activity_12 = (col4.number_input('Enter your PreStartup Planning Planned', min_value=0, max_value=100, step=1)*PreStartup_Planning)/8
	Activity_13 = (col4.number_input('Enter your Startup Training Planned', min_value=0, max_value=100, step=1)*Startup_Training)/8
	Activity_14 = (col4.number_input('Enter your CP Planning Planned', min_value=0, max_value=100, step=1)*CP_Planning)/8
	Activity_15 = (col4.number_input('Enter your BS Planning Planned', min_value=0, max_value=100, step=1)*BS_Planning)/8
	Activity_16 = (col4.number_input('Enter your Consolidation Planned', min_value=0, max_value=100, step=1)*Consolidation)/8
	Activity_17 = (col4.number_input('Enter your Briefings Coach Meetings Planned', min_value=0, max_value=100, step=1)*Briefings_Coach_Meetings)/8
	Activity_18 = (col4.number_input('Enter your Coach Support Time Planned', min_value=0, max_value=100, step=1)*Coach_Support_Time)/8
	Activity_10 = (col4.number_input('Community Engagement for Matching', min_value=0, max_value=100, step=1)*Community_Engagement_for_Matching)/8

	added_activities = (Activity_1+Activity_2+Activity_3+Activity_4+Activity_5+Activity_7+Activity_8
		+Activity_11+Activity_12+Activity_13+Activity_14+Activity_15+Activity_16+Activity_17+Activity_18)

	coach_specific_activities = (Activity_6+Activity_9)

	with col1:
		# Display the filtered data

		# Set the first row as column headers

		df = sum_by_category

		# # Drop the first row to keep it as data
		# df = df.iloc[1:].reset_index(drop=True)
		st.table(df[select_box1].round(0).astype(int))


	with col2:
		st.metric(label="Total Days", value=round(sum_by_category.loc['Total Days', select_box1], 1), delta=+added_activities, delta_color="inverse")
		st.metric(label="BUSINESS AS USUAL (BAU)", value=coach_specific_activities, delta=+12, delta_color="inverse")
		st.metric(label="Overall Days", value=round((sum_by_category.loc['Total Days', select_box1] + 14), 1), delta=+0.5, delta_color="inverse")

	if col4.button('Save Plan'):
		# Create a DataFrame with the entered data
		data = {'Club Meetings': [(Activity_1*8)/Club_Meeting], 'AR': [(Activity_2*8)/AR], 'PQA': [Activity_3],
		'Smartspace': [Activity_4], 'PrePQA': [Activity_5], 'Coaching Circle': [Activity_6],
		'Club leader meetings': [Activity_7], 'Porridge': [Activity_8],'Coach Admin Time': [Activity_9], 
		'Community Engagement for Matching': [Activity_10], 'Matching Day': [Activity_11],
		'PreStartup Planning': [Activity_12], 'Startup Training': [Activity_13], 'CP Planning': [Activity_14],
		'BS Planning': [Activity_15], 'Consolidation': [Activity_16], 'Briefings Coach Meetings': [Activity_17],
		'Support Time': [Activity_18]}
		df = pd.DataFrame(data)


		# Save the DataFrame to an Excel file
		df.to_excel('CoachPlan.xlsx', index=False)
		st.write('Data saved to CoachPlan.xlsx')
	# Create a reset button
	

	with col5:

		st.metric(label="Total Days Left to Complete the Backlog", value=round(sum_by_category.loc['Total Days', select_box1] -added_activities, 1))
		# Create a DataFrame with the entered data
		data = {'Club Meetings': sum_by_category.loc['Club Days', select_box1] - [(Activity_1*8)/Club_Meeting], 'AR': sum_by_category.loc['Annual Reaccreditation', select_box1] - [(Activity_2*8)/AR], 'PQA': sum_by_category.loc['Days PQA', select_box1] - [(Activity_3*8)/PQA],
		'Smartspace': sum_by_category.loc['Day SmartSpace', select_box1] - [(Activity_4*8)/Smartspace], 'PrePQA': [(Activity_5*8)/PrePQA], 'Coaching Circle': [(Activity_6*8)/Coaching_Circle],
		'Club leader meetings': [(Activity_7*8)/Club_leader_meetings], 'Porridge': [(Activity_8*8)/Porridge],'Coach Admin Time': [(Activity_9*8)/Coach_Admin_Time], 
		'Community Engagement for Matching': [(Activity_10*8)/Community_Engagement_for_Matching], 'Matching Day': [(Activity_11*8)/Matching_Day],
		'PreStartup Planning': [(Activity_12*8)/PreStartup_Planning], 'Startup Training': [(Activity_13*8)/Startup_Training], 'CP Planning': sum_by_category.loc['Child Progress Sessions', select_box1] - [(Activity_14*8)/CP_Planning],
		'BS Planning': sum_by_category.loc['Business Skill Sessions', select_box1] - [(Activity_15*8)/BS_Planning], 'Consolidation': [(Activity_16*8)/Consolidation], 'Briefings Coach Meetings': [(Activity_17*8)/Briefings_Coach_Meetings],
		'Support Time': [(Activity_18*8)/Coach_Support_Time]}
		df = pd.DataFrame(data)
		st.table(df.transpose().round(0).astype(int))
		
		

	    
# Club_Meeting = st.sidebar.slider("Club Meeting (hrs)", min_value=2, max_value=5, value=2, step=1)
# AR = st.sidebar.slider("Annual Reaccreditation (hrs)", min_value=2, max_value=10, value=2, step=1)
# PQA = st.sidebar.slider("PQA (hrs)", min_value=4, max_value=10, value=4, step=2)
# Smartspace = st.sidebar.slider("Due for Smartspace (hrs)", min_value=1.5, max_value=6.0, value=1.5, step=0.5)
# PrePQA = st.sidebar.slider("Planning for PQA (PrePQA) (hrs)", min_value=1.5, max_value=5.0, value=1.5, step=0.5)
# Coaching_Circle = st.sidebar.slider("Coaching Circle (hrs)", min_value=2, max_value=10, value=2, step=1)
# Club_leader_meetings = st.sidebar.slider("Club leader meetings (hrs)", min_value=2, max_value=10, value=2, step=1)
# Porridge = st.sidebar.slider("Porridge", min_value=16, max_value=24, value=16, step=1)
# Coach_Admin_Time  = st.sidebar.slider("Coach Admin Time", min_value=8, max_value=12, value=8, step=1)
# Community_Engagement_for_Matching = st.sidebar.slider("Community Engagement for Matching", min_value=24, max_value=30, value=24, step=1)
# Matching_Day  = st.sidebar.slider("Matching Day", min_value=10, max_value=15, value=10, step=1)
# PreStartup_Planning  = st.sidebar.slider("PreStartup Planning", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
# Startup_Training = st.sidebar.slider("Startup Training", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
# CP_Planning = st.sidebar.slider("CP Planning", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
# BS_Planning = st.sidebar.slider("BS Planning", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
# Consolidation  = st.sidebar.slider("Consolidation", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
# Briefings_Coach_Meetings  = st.sidebar.slider("Briefings Coach Meetings", min_value=4, max_value=8, value=4, step=1)
# Coach_Support_Time = st.sidebar.slider("Coach Support Time", min_value=8, max_value=15, value=8, step=1)

	st.subheader(f'_Overall backlog and Summarised work for :blue[{select_box1}]: SmartStart Coach Planning Tool :sunglasses:_')

	cols1, cols2, cols3, cols4, cols5 =st.columns(5)

	

	# st.write(sum_by_category[select_box1])
	cols1.metric(label="Active Franchisees", value=round(sum_by_category.loc['Active Franchisees', select_box1], 0))
	cols2.metric(label="Day SmartSpace", value=sum_by_category.loc['Day SmartSpace', select_box1] - ((Activity_4*8)/Smartspace))
	cols3.metric(label="Days PQA", value=round(sum_by_category.loc['Days PQA', select_box1], 0))
	cols4.metric(label="Club Days", value=round(sum_by_category.loc['Club Days', select_box1], 0))
	cols5.metric(label="Admin Days", value=round(sum_by_category.loc['Admin Days', select_box1], 0))
	# Second Row
	cols1.metric(label="Parcel Days", value=round(sum_by_category.loc['Parcel Days', select_box1], 0))
	cols2.metric(label="Annual Reaccreditation", value=round(sum_by_category.loc['Annual Reaccreditation', select_box1], 0))
	cols3.metric(label="Support Days", value=round(sum_by_category.loc['Support Days', select_box1], 0))
	cols4.metric(label="Child Progress Sessions", value=round(sum_by_category.loc['Child Progress Sessions', select_box1], 0))
	cols5.metric(label="Business Skill Sessions", value=round(sum_by_category.loc['Business Skill Sessions', select_box1], 0))
	# Third Row
	cols1.metric(label="Trainings ", value=round(sum_by_category.loc['Trainings ', select_box1], 0))
	cols2.metric(label="Total Days", value=round(sum_by_category.loc['Total Days', select_box1], 0))

############################################################### COACH SPECIFIC ####################################################


def coach_specific():

	# Get the unique values in the "Franchisor" column
	select_franchisor = model_data["Franchisor"].unique()

	# Create the select box for Franchisor
	select_box1 = st.sidebar.selectbox("Select a Franchisor", select_franchisor)

	# Filter the DataFrame based on the selected Franchisor
	filtered_data = model_data[model_data["Franchisor"] == select_box1]

	# Get the unique values in the "Full Name" (Coach) column from the filtered data
	select_coach = filtered_data["Full Name"].unique()

	# Create the select box for Coach
	select_box2 = st.sidebar.selectbox("Select a Coach", select_coach)

	# Filter the DataFrame based on the selected Coach
	final_data = filtered_data[filtered_data["Full Name"] == select_box2]

	# Add a slider to the sidebar
	Club_Meeting = st.sidebar.slider("Club Meeting (hrs)", min_value=2, max_value=5, value=2, step=1)
	AR = st.sidebar.slider("Annual Reaccreditation (hrs)", min_value=2, max_value=10, value=2, step=1)
	PQA = st.sidebar.slider("PQA (hrs)", min_value=4, max_value=10, value=4, step=2)
	Smartspace = st.sidebar.slider("Smartspace (hrs)", min_value=1.5, max_value=6.0, value=1.5, step=0.5)
	PrePQA = st.sidebar.slider("PrePQA (hrs)", min_value=1.5, max_value=5.0, value=1.5, step=0.5)
	Coaching_Circle = st.sidebar.slider("Coaching Circle (hrs)", min_value=2, max_value=10, value=2, step=1)
	Club_leader_meetings = st.sidebar.slider("Club leader meetings (hrs)", min_value=2, max_value=10, value=2, step=1)
	Porridge = st.sidebar.slider("Porridge", min_value=16, max_value=24, value=16, step=1)
	Coach_Admin_Time  = st.sidebar.slider("Coach Admin Time", min_value=8, max_value=12, value=8, step=1)
	Community_Engagement_for_Matching = st.sidebar.slider("Community Engagement for Matching", min_value=24, max_value=30, value=24, step=1)
	Matching_Day  = st.sidebar.slider("Matching Day", min_value=10, max_value=15, value=10, step=1)
	PreStartup_Planning  = st.sidebar.slider("PreStartup Planning", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
	Startup_Training = st.sidebar.slider("Startup Training", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
	CP_Planning = st.sidebar.slider("CP Planning", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
	BS_Planning = st.sidebar.slider("BS Planning", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
	Consolidation  = st.sidebar.slider("Consolidation", min_value=3.0, max_value=5.0, value=3.0, step=0.5)
	Briefings_Coach_Meetings  = st.sidebar.slider("Briefings Coach Meetings", min_value=4, max_value=8, value=4, step=1)
	Coach_Support_Time = st.sidebar.slider("Coach Support Time", min_value=8, max_value=15, value=8, step=1)


	st.subheader(f'_Overall Backlog and Summarised work for :blue[{select_box2}]: A detailed SmartStart Coach Plan :purple_heart:_')

	c1, c2 = st.columns(2)

	
	c1.subheader("_Backlog represented by days to complete._")

	# c1.markdown("Backlog for the Franchisor: See the performance against the backlog and the hours it will take to complete.")
	c2.subheader("_Planning represented by days to complete._")

	col1, col2, col3, col4, col5 = st.columns((1, 1, 1, 1,1))

	# options = ["Coach Plan", "Due on SmartLink", "Franchisor Information", "Training Plan on SmartLink or IP"]

	# # Create a selectbox for choosing the option
	# selected_option = col3.selectbox('Select Data:', options)

	Activity_1 = (col3.number_input('Enter your Club Meetings Planned', min_value=0, max_value=100, step=1)*Club_Meeting)/8
	Activity_2 = (col3.number_input('Enter your AR Planned', min_value=0, max_value=100, step=1)*AR)/8
	Activity_3 = (col3.number_input('Enter your PQA Planned', min_value=0, max_value=100, step=1)*PQA)/8
	Activity_4 = (col3.number_input('Enter your Smartspace Planned', min_value=0, max_value=100, step=1)*Smartspace)/8
	Activity_5 = (col3.number_input('Enter your PrePQA Planned', min_value=0, max_value=100, step=1)*PrePQA)/8
	Activity_6 = (col3.number_input('Enter your Coaching Circle Planned', min_value=0, max_value=100, step=1)*Coaching_Circle)/8
	Activity_7 = (col3.number_input('Enter your Club leader meetings Planned', min_value=0, max_value=100, step=1)*Club_leader_meetings)/8
	Activity_8 = (col3.number_input('Enter your Porridge Planned', min_value=0, max_value=100, step=1)*Porridge)/8
	Activity_9 = (col3.number_input('Coach Admin Time', min_value=0, max_value=100, step=1)*Coach_Admin_Time)/8
	Activity_11 = (col4.number_input('Enter your Matching Day Planned', min_value=0, max_value=100, step=1)*Matching_Day)/8
	Activity_12 = (col4.number_input('Enter your PreStartup Planning Planned', min_value=0, max_value=100, step=1)*PreStartup_Planning)/8
	Activity_13 = (col4.number_input('Enter your Startup Training Planned', min_value=0, max_value=100, step=1)*Startup_Training)/8
	Activity_14 = (col4.number_input('Enter your CP Planning Planned', min_value=0, max_value=100, step=1)*CP_Planning)/8
	Activity_15 = (col4.number_input('Enter your BS Planning Planned', min_value=0, max_value=100, step=1)*BS_Planning)/8
	Activity_16 = (col4.number_input('Enter your Consolidation Planned', min_value=0, max_value=100, step=1)*Consolidation)/8
	Activity_17 = (col4.number_input('Enter your Briefings Coach Meetings Planned', min_value=0, max_value=100, step=1)*Briefings_Coach_Meetings)/8
	Activity_18 = (col4.number_input('Enter your Coach Support Time Planned', min_value=0, max_value=100, step=1)*Coach_Support_Time)/8
	Activity_10 = (col4.number_input('Community Engagement for Matching', min_value=0, max_value=100, step=1)*Community_Engagement_for_Matching)/8



	added_activities = (Activity_1+Activity_2+Activity_3+Activity_4+Activity_5+Activity_7+Activity_8
		+Activity_11+Activity_12+Activity_13+Activity_14+Activity_15+Activity_16+Activity_17+Activity_18)

	coach_specific_activities = (Activity_6+Activity_9)

	with col1:
		# Display the filtered data

		# Set the first row as column headers

		df = final_data.transpose()
		df.columns = df.iloc[0]

		# # Drop the first row to keep it as data
		# df = df.iloc[1:].reset_index(drop=True)
		st.table(df)
		# st.write(df)

	with col2:
		st.metric(label="Total Days", value=round(final_data['Total Days'], 1), delta=+added_activities, delta_color="inverse")
		st.metric(label="BUSINESS AS USUAL (BAU)", value=coach_specific_activities, delta=-coach_specific_activities, delta_color="inverse")
		st.metric(label="Overall Days", value=round((final_data['Total Days'] + coach_specific_activities), 1), delta=+0.5, delta_color="inverse")

	if col4.button('Save Plan'):
		# Create a DataFrame with the entered data
		data = {'Club Meetings': [Activity_1], 'AR': [Activity_2], 'PQA': [Activity_3],
		'Smartspace': [Activity_4], 'PrePQA': [Activity_5], 'Coaching Circle': [Activity_6],
		'Club leader meetings': [Activity_7], 'Porridge': [Activity_8],'Coach Admin Time': [Activity_9], 
		'Community Engagement for Matching': [Activity_10], 'Matching Day': [Activity_11],
		'PreStartup Planning': [Activity_12], 'Startup Training': [Activity_13], 'CP Planning': [Activity_14],
		'BS Planning': [Activity_15], 'Consolidation': [Activity_16], 'Briefings Coach Meetings': [Activity_17],
		'Support Time': [Activity_18]}
		df = pd.DataFrame(data)


		# Save the DataFrame to an Excel file
		df.to_excel('CoachPlan.xlsx', index=False)
		st.write('Data saved to CoachPlan.xlsx')

	with col5:

		# Show A metric showing the number of total dAYS LEFT
		st.metric(label="Total Days Left to Complete the Backlog", value=round(sum_by_category.loc['Total Days', select_box1] -added_activities, 1))
		# Create a DataFrame with the entered data
		data = {'Club Meetings': sum_by_category.loc['Club Days', select_box1] - [(Activity_1*8)/Club_Meeting], 'AR': sum_by_category.loc['Annual Reaccreditation', select_box1] - [(Activity_2*8)/AR], 'PQA': sum_by_category.loc['Days PQA', select_box1] - [(Activity_3*8)/PQA],
		'Smartspace': sum_by_category.loc['Day SmartSpace', select_box1] - [(Activity_4*8)/Smartspace], 'PrePQA': [(Activity_5*8)/PrePQA], 'Coaching Circle': [(Activity_6*8)/Coaching_Circle],
		'Club leader meetings': [(Activity_7*8)/Club_leader_meetings], 'Porridge': [(Activity_8*8)/Porridge],'Coach Admin Time': [(Activity_9*8)/Coach_Admin_Time], 
		'Community Engagement for Matching': [(Activity_10*8)/Community_Engagement_for_Matching], 'Matching Day': [(Activity_11*8)/Matching_Day],
		'PreStartup Planning': [(Activity_12*8)/PreStartup_Planning], 'Startup Training': [(Activity_13*8)/Startup_Training], 'CP Planning': sum_by_category.loc['Child Progress Sessions', select_box1] - [(Activity_14*8)/CP_Planning],
		'BS Planning': sum_by_category.loc['Business Skill Sessions', select_box1] - [(Activity_15*8)/BS_Planning], 'Consolidation': [(Activity_16*8)/Consolidation], 'Briefings Coach Meetings': [(Activity_17*8)/Briefings_Coach_Meetings],
		'Support Time': [(Activity_18*8)/Coach_Support_Time]}
		df = pd.DataFrame(data)
		st.table(df.transpose())
	    # st.metric(label="Total Days Left to Complete the Backlog", value=round(final_data['Total Days'] -added_activities, 1), delta=-added_activities, delta_color="inverse")
	    # st.metric(label="BUSINESS AS USUAL (BAU)", value=coach_specific_activities, delta=-coach_specific_activities, delta_color="inverse")
	    # st.metric(label="Total Days Left to Complete Tasks", value=(round(final_data['Total Days'] - added_activities - coach_specific_activities, 1)), delta=+coach_specific_activities, delta_color="inverse")

	st.subheader(f'_Overall backlog and Summarised work for :blue[{select_box1}]: SmartStart Coach Planning Tool :sunglasses:_')

	cols1, cols2, cols3, cols4, cols5 =st.columns(5)

	

	# st.write(sum_by_category[select_box1])
	cols1.metric(label="Active Franchisees", value=round(sum_by_category.loc['Active Franchisees', select_box1], 0))
	cols2.metric(label="Day SmartSpace", value=round(sum_by_category.loc['Day SmartSpace', select_box1]  - ((Activity_4*8)/Smartspace), 0))
	cols3.metric(label="Days PQA", value=round(sum_by_category.loc['Days PQA', select_box1], 0))
	cols4.metric(label="Club Days", value=round(sum_by_category.loc['Club Days', select_box1], 0))
	cols5.metric(label="Admin Days", value=round(sum_by_category.loc['Admin Days', select_box1] + Activity_9, 0))
	# Second Row
	cols1.metric(label="Parcel Days", value=round(sum_by_category.loc['Parcel Days', select_box1], 0))
	cols2.metric(label="Annual Reaccreditation", value=round(sum_by_category.loc['Annual Reaccreditation', select_box1], 0))
	cols3.metric(label="Support Days", value=round(sum_by_category.loc['Support Days', select_box1], 0))
	cols4.metric(label="Child Progress Sessions", value=round(sum_by_category.loc['Child Progress Sessions', select_box1], 0))
	cols5.metric(label="Business Skill Sessions", value=round(sum_by_category.loc['Business Skill Sessions', select_box1], 0))
	# Third Row
	cols1.metric(label="Trainings ", value=round(sum_by_category.loc['Trainings ', select_box1], 0))
	cols2.metric(label="Total Days", value=round(sum_by_category.loc['Total Days', select_box1], 0))
	# cols3.metric(label="Days PQA", value=round(sum_by_category.loc['Days PQA', select_box1], 0))
	# cols4.metric(label="Club Days", value=round(sum_by_category.loc['Club Days', select_box1], 0))
	# cols5.metric(label="Admin Days", value=round(sum_by_category.loc['Admin Days', select_box1], 0))


# Define a list of page names

pages = ["Model", "Franchisor Planning", "Coach Planning"]

# Add a selectbox widget to select the page
page_index = st.sidebar.selectbox("Select Page", pages)

# Render the selected page
if page_index == "Model":
    model()
if page_index == "Franchisor Planning":
    franchisor()
if page_index == "Coach Planning":
    coach_specific()


