def print_args(var1=None, var2=None, var3=None):
    args = {k: v for k, v in locals().items() if k.startswith('var')}
    print("Переданы аргументы:", ', '.join(f"{k} = {v}" for k, v in args.items() if v is not None) or 'отсутствуют')

# Тесты
print_args(var1=2)
print_args(var2=3, var3=10)
print_args()
print_args(var1=None)
