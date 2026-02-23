

print("=== Hospital Billing System ===")

patient_name = input("Enter patient name: ")
room_days = int(input("Enter number of days admitted: "))
lab_fee = float(input("Enter laboratory fee: "))
doctor_fee = float(input("Enter doctor's fee: "))

room_rate = 1500
room_total = room_days * room_rate

total_bill = room_total + lab_fee + doctor_fee

print("\n--- BILL SUMMARY ---")
print("Patient Name:", patient_name)
print("Room Charges:", room_total)
print("Laboratory Fee:", lab_fee)
print("Doctor's Fee:", doctor_fee)
print("Total Bill:", total_bill)