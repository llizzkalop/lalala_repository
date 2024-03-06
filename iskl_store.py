import warnings

def function_with_warning():
        try:
            print('Генерация возможного предупреждения')
            warnings.warn("*Не игнорируй это предупреждение*", UserWarning)
            print()
        except UserWarning as e:
            print(f'Предупреждение было перехвачено,в качестве исключения - {e}')
        else:
            print('Предупреждения проигнорированы.')


print("Пример 1: Фильтр - 'error'")
warnings.simplefilter('error', UserWarning)
function_with_warning()
print("\n")

print("Пример 1: Фильтр - 'ignore'")
warnings.simplefilter('ignore', UserWarning)
function_with_warning()
print("\n")


