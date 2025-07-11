from time import time
from datetime import datetime

def main():
    sum_seconds = time()
    print(f"Seconds since January 1, 1970: {sum_seconds:,.4f} or {sum_seconds:.2e} 9 in scientific notation")

    current_date = datetime.today().strftime("%b %d %Y")
    print(current_date)

if __name__ == "__main__":
    main()