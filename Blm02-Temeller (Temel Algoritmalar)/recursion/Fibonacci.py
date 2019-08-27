def fibonacci(sayi):
    if (sayi <= 2):
        return 1
    else:
        return fibonacci(sayi - 2) + fibonacci(sayi - 1)
