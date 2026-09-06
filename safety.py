print(" ELECTRICAL SAFETY STANDARDS SYSTEM")
print("1. IEEE")
print("2. IEC")
print("3. NFPA")
print("4. OSHA")
print("5. BIS")
print("6. Exit")
choice = input("Enter your choice: ")
if choice == "1":
    print("\nIEEE")
    print("Purpose: Provides electrical engineering standards.")
    print("Application: Arc-flash analysis, power systems and safety studies.")
elif choice == "2":
    print("\nIEC")
    print("Purpose: Develops international electrical standards.")
    print("Application: Electrical installations and equipment safety.")
elif choice == "3":
    print("\nNFPA")
    print("Purpose: Provides electrical safety requirements.")
    print("Application: Electrical installations and workplace safety.")
elif choice == "4":
    print("\nOSHA")
    print("Purpose: Provides workplace safety requirements.")
    print("Application: Worker protection and electrical safety.")
elif choice == "5":
    print("\nBIS")
    print("Purpose: Develops Indian electrical standards.")
    print("Application: Wiring, earthing and electrical installations.")
elif choice == "6":
    print("\nProgram ended.")
else:
    print("\nInvalid choice.")