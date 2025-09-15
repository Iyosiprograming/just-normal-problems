print("************** Hospital Patient Queue System ****************")

howmanypatient = int(input("Enter How Many Patients?: "))

patients = []

for i in range(howmanypatient):
    print(f"\nPatient {i+1}")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    severity = int(input("Enter Patient Severity (1 to 10, 1=good, 10=bad): "))

    patients.append({
        "name": name,
        "age": age,
        "severity": severity
    })

patients_sorted = sorted(
    patients,
    key=lambda x: (x["severity"], x["age"]),
    reverse=True
)

print("\n--- Treatment Order ---")
for idx, patient in enumerate(patients_sorted, start=1):
    print(f"{idx}. {patient['name']} (Age: {patient['age']}, Severity: {patient['severity']})")
