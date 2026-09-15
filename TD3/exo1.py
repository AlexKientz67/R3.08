def divise(a : float, b : float):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error : Division by zero"
    except TypeError:
        return "Error : Type Error"
    except ValueError:
        return "Error : Value Error"

if __name__ == "__main__":
    x = 5
    y = 0
    print(divise(x, y))
