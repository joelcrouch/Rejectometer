import pandas as pd
import random
from faker import Faker

# Initialize Faker for generating random names
fake = Faker()

# List of possible values for the variables
organ_types = ['Kidney', 'Liver', 'Heart', 'Lung']
genders = ['Male', 'Female']
diseases = ['End-stage Kidney Disease', 'Cirrhosis', 'Heart Failure', 'Lung Disease']
immunosuppressants = ['Tacrolimus', 'Mycophenolate', 'Prednisone', 'Cyclosporine']
death_reasons = ['Cardiac Arrest', 'Infection', 'Organ Rejection', 'Stroke', 'Other']

# Number of patients to generate
num_patients = 100

# Generate mock data
data = []

for i in range(num_patients):
    patient_id = fake.uuid4()
    donor_id = fake.uuid4()
    age_recipient = random.randint(18, 75)
    age_donor = random.randint(18, 75)
    gender_recipient = random.choice(genders)
    gender_donor = random.choice(genders)
    organ_type = random.choice(organ_types)
    disease = random.choice(diseases)
    transplant_date = fake.date_this_decade()
    immunosuppressant = random.choice(immunosuppressants)
    rejection_event = random.choice([True, False])
    rejection_time = random.randint(30, 365) if rejection_event else None
    survival_time = random.randint(30, 3650)  # Survival time in days (up to 10 years)
    death_event = random.choice([True, False])
    cause_of_death = random.choice(death_reasons) if death_event else None

    # Store the data
    data.append({
        'Patient_ID': patient_id,
        'Donor_ID': donor_id,
        'Age_Recipient': age_recipient,
        'Age_Donor': age_donor,
        'Gender_Recipient': gender_recipient,
        'Gender_Donor': gender_donor,
        'Organ_Type': organ_type,
        'Disease': disease,
        'Transplant_Date': transplant_date,
        'Immunosuppressant': immunosuppressant,
        'Rejection_Event': rejection_event,
        'Rejection_Time': rejection_time,
        'Survival_Time': survival_time,
        'Death_Event': death_event,
        'Cause_of_Death': cause_of_death
    })

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Display the first few rows
print(df.head())
