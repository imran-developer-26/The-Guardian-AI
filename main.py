# --- The Guardian of Justice AI ---
# Developer: Adnan (Professional System Architect)
# Version: 1.0 (GitHub Edition)

# 1. Initialize System Data
trust_score = 100
is_active = True

print("--- [SYSTEM INITIALIZED]: The Guardian AI is Online ---")
print("--- Developed for GitHub Portfolio Project ---\n")

# 2. Main Audit Loop (Keeps the system running)
while trust_score > 70:
    # Display Current Status
    print(f"Current System Status - Trust Score: {trust_score}%")
    
    # Identify the User (Unique Identity)
    driver_name = input("Enter Driver's Name: ")
    license_no = input("Enter Driving License Number: ")
    
    print(f"\n[SCANNING]: Checking profile for {driver_name} (ID: {license_no})...")
    
    # 3. Emergency & Decision Logic
    emergency_claim = input("Is this a medical emergency? (yes/no): ").lower()
    
    if emergency_claim == "yes":
        action = "PROCEED: Priority lane opened. Waiting for evidence."
        print(f">> Decision: {action}")
    else:
        # Deduct 10 points for unnecessary bypass
        trust_score -= 10 
        action = f"DENIED: Normal lane. Trust Score reduced to {trust_score}%"
        print(f">> Decision: {action}")

    # 4. Persistent Data Storage (Audit Log)
    # Using utf-8 encoding to support all characters and avoid errors
    with open("audit_report.txt", "a", encoding="utf-8") as report_file:
        log_entry = f"Driver: {driver_name} | License: {license_no} | Action: {action}\n"
        report_file.write(log_entry)
        print("--- [SUCCESS]: Audit report saved to database ---")

    # 5. Multi-level Warning System
    if trust_score < 80:
        print("\n[HIGH ALERT]: Trust Score is Critical!")
        print("Action: Sending full report to Local Council for monitoring.")
        break # System locks down when score falls below 80
    elif trust_score < 95:
        print("\n[SYSTEM WARNING]: Trust Score is dropping. Please follow traffic rules.")

print("\n--- [SYSTEM SHUTDOWN]: Audit complete. Review audit_report.txt for details ---")