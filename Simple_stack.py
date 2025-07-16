# Simple Process Stack Manager

process_stack = []

while True:
    print('\n--- Process Stack ---')
    print('[i] Include new process')
    print('[r] Remove (pop) last process')
    print('[e] Exit')
    choice = input('Your choice: ').strip().lower()

    if choice == 'i':
        process_number = input('Enter process number: ')
        process_name = input('Enter process name: ')
        process = {
            'number': process_number,
            'name': process_name
        }
        process_stack.append(process)
        print('Process added.')

    elif choice == 'r':
        if process_stack:
            removed = process_stack.pop()
            print(f'Removed process: {removed}')
        else:
            print('Stack is empty!')

    elif choice == 'e':
        print('Exiting. Final stack state:')
        for idx, proc in enumerate(process_stack, 1):
            print(f"{idx}: {proc}")
        break

    else:
        print('Invalid option. Try again.')
