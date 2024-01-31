def line(deli_line):
    if len(deli_line) == 0:
        print("The line is currently empty.")
    else:
        line_order = []
        count = 0
        while count < len(deli_line):
            line_order.append(f"{count + 1}. {deli_line[count]}")
            count += 1
        line_string = " ".join(line_order)
        print(f"The line is currently: {line_string}")

def take_a_number(curr_line, customer):
    curr_line.append(customer)
    print(f"Welcome, {customer}. You are number {len(curr_line)} in line.")

def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {line[0]}.")
        del line[0]