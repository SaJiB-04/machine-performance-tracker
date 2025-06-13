def get_daily_inputs(prompt):
    daily_values = []
    for day in range(7):
        while True:
            try:
                value = float(input(f"{prompt} Day {day + 1}:"))
                daily_values.append(value)
                break
            except ValueError:
                print("Invalid Input!")
    return daily_values
def collect_machine_data(num_machines):
    op_hr = []
    dt_hr = []
    defects = []
    for i in range(num_machines):
        print(f"\nMachine {i + 1} Data Collection:")
        op_hr.append(get_daily_inputs("  Operation hours "))
        dt_hr.append(get_daily_inputs("  Downtime hours "))
        defects.append(get_daily_inputs("  Defects "))
    return op_hr,dt_hr,defects
def calculate_metrics(op_hr,dt_hr,defects):
    report_lines = ["\n=== Machine Performance Report ==="]
    for i in range(len(op_hr)):
        total_op = sum(op_hr[i])
        total_dt = sum(dt_hr[i])
        total_def = sum(defects[i])
        total_time = total_op + total_dt
        efficiency = (total_op / total_time) * 100 if total_time > 0.0 else 0.0
        report_lines.append(
            f"\n Machine {i + 1}:\n"
            f"  Total operation hours : {total_op:.2f}\n"
            f"  Total Downtime        : {total_dt:.2f}\n"
            f"  Total Defects         : {total_def:.0f}\n"
            f"  Efficiency            : {efficiency:.2f}\n"
        )
    return "\n".join(report_lines)
import csv
def save_csv(op_hr,dt_hr,defects,file_path = "machine_data.csv"):
    with open(file_path,"w",newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Machine","Day","Operation Hours","Downtime Hours","Defects"])
        num_machines = len(op_hr)
        for machine in range(num_machines):
            for day in range(7):
                writer.writerow([
                    machine + 1,
                    day + 1,
                    op_hr[machine][day],
                    dt_hr[machine][day],
                    defects[machine][day]
                ])
    print(f"Machine Data saved to '{file_path}'!")


def save_report(text,file_path = "performance_tracker.txt"):
    with open(file_path,"w") as f:
         f.write(text)
    print(f"\nReport added to '{file_path}'!")
def main():
    num_machines = int(input("Enter number of machines:"))
    op_hr,dt_hr,defects = collect_machine_data(num_machines)
    report = calculate_metrics(op_hr,dt_hr,defects)
    print(report)
    save_report(report)
    save_csv(op_hr,dt_hr,defects)
main()



