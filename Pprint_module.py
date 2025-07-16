import pprint

process_stack = []

while True:
    print('\n--- Process Stack Manager ---')
    print('1. Add process')
    print('2. Remove (pop) last process')
    print('3. Clear all processes and exit')

    try:
        option = int(input('Your choice: '))
    except ValueError:
        print('Please enter a valid number.')
        continue

    if option == 1:
        name = input('Enter process name: ')
        description = input('Enter process description: ')
        process = {
            'name': name,
            'description': description
        }
        process_stack.append(process)
        print('Process added:')
        pprint.pprint(process)
    elif option == 2:
        if process_stack:
            removed = process_stack.pop()
            print('Removed process:')
            pprint.pprint(removed)
            print('Current stack:')
            pprint.pprint(process_stack)
        else:
            print('Stack is empty!')
    elif option == 3:
        process_stack.clear()
        print('Process stack cleared. Exiting...')
        break
    else:
        print('Invalid option. Please select 1, 2, or 3.')

print('End of program.')
