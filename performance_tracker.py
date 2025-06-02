num_of_machines = int(input("Enter number of machines:"))
operation_hours = []
for machine  in range(num_of_machines):
    print(f"\nEnter operation hours for machine {machine + 1}:")
    daily_hours = []
    for day in range(7):
        hours = float(input(f" Day {day + 1}:"))
        daily_hours.append(hours)
    operation_hours.append(daily_hours)
for i,hours in enumerate(operation_hours):
    print(f"Machine {i + 1} operation hours: {hours} ")
downtime_hours = []
for machine in range(num_of_machines):
    print(f"\nEnter downtime hours for machine {machine + 1}:")
    daily_dt_hours = []
    for day in range(7):
        dt_hours = float(input(f" Day {day + 1}:"))
        daily_dt_hours.append(dt_hours)
    downtime_hours.append(daily_dt_hours)
for i,hours in enumerate(downtime_hours):
    print(f"Machine {i + 1} downtime hours: {hours}")
number_of_defects = []
for machine in range(num_of_machines):
    print(f"\nEnter number of defects for machine {machine + 1}:")
    daily_def = []
    for day in range(7):
        defect = float(input(f" Day {day + 1}:"))
        daily_def.append(defect)
    number_of_defects.append(daily_def)
for i,defect in enumerate(number_of_defects):
    print(f"Machine {i +1} number of defects: {defect}")
print("\n=== Machine Performance Report ===")
for machine in range(num_of_machines):
    total_op = sum(operation_hours[machine])
    total_down = sum(downtime_hours[machine])
    total_def = sum(number_of_defects[machine])


    total_time = total_op + total_down
    if total_time > 0:
        efficiency = (total_op / total_time) * 100
    else:
        efficiency = 0.0
    print(f"\nMachine {machine + 1}:")
    print(f"  Total operation hours  :  {total_op:.2f}")
    print(f"  Total downtime hours   :  {total_down:.2f}")
    print(f"  Total Defects          :  {total_def:.0f}")
    print(f"  Efficiency             :  {efficiency:.2f}%")
report = ""
report += "\n=== Machine Performance Report ===\n"
for machine in range(num_of_machines):
    total_op = sum(operation_hours[machine])
    total_down = sum(downtime_hours[machine])
    total_def = sum(number_of_defects[machine])

    total_time = total_op + total_down
    efficiency = (total_op / total_time) * 100 if total_time > 0 else 0.0

    report += f"\nMachine {machine + 1}:\n"
    report += f"    Total operation hours   :  {total_op:.2f}\n"
    report += f"    Total downtime hours    :  {total_down:.2f}\n"
    report += f"    Total Defects           :  {total_def:.0f}\n"
    report += f"    Efficiency              :  {efficiency:.2f}%\n"

file_path = "performance_report.txt"
with open(file_path,"w") as file:
    file.write(report)

print(f"Report Saved to '{file_path}'")