import math
import time
import os


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def format_custom(val):
    try:
        str_val = str(val).strip()
        if str_val == "0" or str_val == "0.0" or val == 0:
            return "0.00e0"
            

        if str_val.startswith("-"):
            return f"-{format_custom(str_val[1:])}"

        int_val = int(float(str_val)) if "." in str_val else int(str_val)

        if int_val < 1_000_000_000_000:
            return f"{int_val:,.2f}"
        log_val = math.log10(int_val)
        return format_from_log_layers(0, log_val)
        
    except Exception as e:
        # Fallback if anything unexpected goes wrong
        return format_from_log_layers(1, 1)




import math

def format_from_log_layers(layers, top_value):
    letters = ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    current_val = top_value
    tier = layers

    while current_val >= 1000000000000 and tier < len(letters) - 1:
        current_val = math.log10(current_val)
        tier += 1

    while current_val < 0 and tier > 0:
        current_val = 10 ** current_val
        tier -= 1

    exponent = int(current_val)
    mantissa = 10 ** (current_val - exponent)
    return f"{mantissa:.2f}{letters[tier]}{exponent}"

def format_custom(val):
    try:
        str_val = str(val).strip()
        if str_val in ("0", "0.0") or val == 0:
            return "0.00e0"
        if str_val.startswith("-"):
            return f"-{format_custom(str_val[1:])}"
        int_val = int(float(str_val)) if "." in str_val else int(str_val)
        if int_val < 1000000000000:
            return f"{int_val:,.2f}"
        log_val = math.log10(int_val)
        return format_from_log_layers(0, log_val)
    except:
        return format_from_log_layers(1, 1)


while True:
    clear_screen()
    print("=" * 70)

    print("well, welcome to the big calculator thing ing")
    print("choose an option")

    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")
    print("5. exponentiation")
    print("6. tetration")
    print("7. pentation")
    print("8. fibonacci sequence")
    print("9. hexation")
    print("10. exit")
    
    print("=" * 70)

    input1 = input("choose an option: ")

    if input1 == "10":
        print("Goodbye!")
        break

    if input1 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Invalid option, please choose again.")
        time.sleep(1)
        continue

    if input1 == "8":
        try:
            n_terms = int(
                input("Enter the number of terms for the Fibonacci sequence: "))
            if n_terms <= 0:
                print("Please enter a positive integer.")
            else:
                a, b = 0, 1
                for i in range(n_terms):
                        if i == 0:
                            print((a))
                        elif i == 1:
                            print((b))
                        else:
                            c = a + b
                            a = b
                            b = c
                            print(format_custom(b))
                            if n_terms <= 100:
                                time.sleep(0.05)
                            if n_terms <= 1000:
                                time.sleep(0.01)
                            if n_terms <= 10000:
                                time.sleep(0.001)
        except ValueError:
            print("Invalid input! Please enter an integer.")
        input("\nPress Enter to return to the menu...")
        continue

    input2 = float(input("enter the first number: "))
    input3 = float(input("enter the second number: "))

    if input1 == "1":
        print(format_custom(input2 + input3))
    elif input1 == "2":
        print(format_custom(input2 - input3))
    elif input1 == "3":
        print(format_custom(input2 * input3))
    elif input1 == "4":
        if input3 == 0:
            print("Error: Division by zero!")
        else:
            print(format_custom(input2 / input3))
    elif input1 == "5":
        try:
            val = input2 ** input3
            print(format_custom(val))
        except OverflowError:
            print(format_from_log_layers(0, input3 * math.log10(input2)))
    elif input1 in ["6", "7", "9"]:
        try:
            b = input2
            h = input3

            if b <= 1.0 or h <= 0.0:
                print("1.00e0")
                input("\nPress Enter to return to the menu...")
                continue

            log_b = math.log10(b)

            if input1 == "6":
                try:
                    log_val = (h ** b) * log_b
                    print(format_from_log_layers(0, log_val))
                except:
                    log_h = math.log10(h)
                    print(format_from_log_layers(
                        1, b * log_h + math.log10(log_b)))
            elif input1 == "7":
                try:
                    inner = (b ** h) * math.log10(b)
                    log_val = (b ** inner) * log_b
                    print(format_from_log_layers(0, log_val))
                except:
                    print(format_from_log_layers(2, h * log_b))
            elif input1 == "9":
                try:
                    inner2 = (h ** b) * log_b
                    inner1 = (b ** inner2) * log_b
                    log_val = (b ** inner1) * log_b
                    print(format_from_log_layers(0, log_val))
                except:
                    print(format_from_log_layers(3, h * log_b))
        except Exception:
            print("you LITERALLY CROSSED THE UNIVERSES BOUNDARIES WHAT")

    input("\nPress Enter to return to the menu...")
