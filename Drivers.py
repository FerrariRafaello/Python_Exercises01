from typing import List

# List to store all drivers and their laps
drivers_queue = []

def clear_screen():
    print('\n' * 50)

def menu() -> int:
    print('[1] Add driver')
    print('[2] Remove driver')
    print('[3] Show drivers')
    print('[4] Show ranking')
    print('[5] Exit')
    option = input('Choose an option: ')
    return int(option)

def create_driver() -> dict:
    clear_screen()
    name = input('Enter driver name: ')
    num_laps = int(input('How many laps did the driver complete? '))
    laps = []
    for i in range(1, num_laps + 1):
        lap_time = float(input(f'Enter lap {i} time (seconds): '))
        laps.append(lap_time)
    driver = {
        'name': name,
        'laps': laps,
        'average': sum(laps) / len(laps) if laps else 0
    }
    return driver

def add_driver():
    driver = create_driver()
    drivers_queue.append(driver)
    input('Driver registered. Press <enter> to continue.')

def remove_driver():
    clear_screen()
    if not drivers_queue:
        print('No drivers in the queue.')
        input('Press <enter> to return to menu.')
        return
    print('Current drivers:')
    for idx, driver in enumerate(drivers_queue, 1):
        print(f'[{idx}] {driver["name"]}')
    idx_to_remove = int(input('Enter the number of the driver to remove: '))
    if 1 <= idx_to_remove <= len(drivers_queue):
        removed = drivers_queue.pop(idx_to_remove - 1)
        print(f'Driver {removed["name"]} removed.')
    else:
        print('Invalid number.')
    input('Press <enter> to continue.')

def show_drivers():
    clear_screen()
    if not drivers_queue:
        print('No drivers registered.')
    else:
        print('Registered drivers:')
        for driver in drivers_queue:
            print(f'- {driver["name"]}: laps = {driver["laps"]} | avg = {driver["average"]:.2f}s')
    input('Press <enter> to return to menu.')

def show_ranking():
    clear_screen()
    if not drivers_queue:
        print('No drivers for ranking.')
    else:
        ranked = sorted(drivers_queue, key=lambda d: d['average'])
        print('Ranking (by best average lap):')
        for pos, driver in enumerate(ranked, 1):
            print(f'{pos}. {driver["name"]} | Avg: {driver["average"]:.2f}s | Laps: {driver["laps"]}')
    input('Press <enter> to return to menu.')

# Main loop
while True:
    option = menu()
    if option == 1:
        add_driver()
    elif option == 2:
        remove_driver()
    elif option == 3:
        show_drivers()
    elif option == 4:
        show_ranking()
    elif option == 5:
        print('Session ended by user.')
        break
    else:
        print('Invalid option!')

