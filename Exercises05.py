#---------------------------#
# Area of a rectangle

length = float(input('Enter the length: '))
width = float(input('Enter the width: '))
area = length * width
print('The area is:', area)

#---------------------------#
# Fahrenheit to Celsius

f = float(input('Enter degrees Fahrenheit: '))
c = 5 * ((f - 32) / 9)
print('In Celsius: %.2f' % c)

#---------------------------#
# Celsius to Fahrenheit

cel = float(input('In Celsius: '))
f = (cel * 1.8) + 32
print(f'In Fahrenheit: {f:.2f}')

#---------------------------#
# Fishing excess calculation

weight = float(input('Total fish weight today (kg)? '))
excess = max(weight - 50, 0)
fine = excess * 4
print(f'Total fished: {weight:.2f}, excess: {excess:.2f}, fine: R$ {fine:.2f}')

#---------------------------#
# Ideal weight by gender

gender = input('Are you [h] or [m]? ').lower()
if gender == 'h':
    height = float(input('Enter your height (m): '))
    ideal_weight = (72.7 * height) - 58
    print(f'Your ideal weight is: {ideal_weight:.2f}')
elif gender == 'm':
    height = float(input('Enter your height (m): '))
    ideal_weight = (62.1 * height) - 44.7
    print(f'Your ideal weight is: {ideal_weight:.2f}')
else:
    print('Invalid input for gender.')

#----------------------------#
# Salary breakdown

hourly_rate = float(input('Amount earned per hour: '))
hours_month = int(input('Hours worked per month: '))
salary = hours_month * hourly_rate
ir = salary * 0.11
inss = salary * 0.08
union = salary * 0.05
net = salary - ir - inss - union
print(f'Gross salary: {salary:.2f}')
print(f'IR deduction: {ir:.2f}')
print(f'INSS deduction: {inss:.2f}')
print(f'Union deduction: {union:.2f}')
print(f'Net salary: {net:.2f}')

#----------------------------#
# Integer and real input calculations

int1 = int(input('Enter the first integer: '))
int2 = int(input('Enter the second integer: '))
real = float(input('Enter a real number: '))
a = (int1 * 2) + (int2 / 2)
b = (int1 * 3) + real
c = real ** 3
print(f'{a:.2f}, {b:.2f}, {c:.2f}')

#----------------------------#
# Paint calculation (simple version)

area = int(input('Enter area in square meters to be painted: '))
liters_needed = area / 3
cans_needed = liters_needed / 18
total_cost = cans_needed * 80
print(f'To paint the area, you need {liters_needed:.2f} liters, which is {cans_needed:.2f} cans, costing {total_cost:.2f}.')

#---------------------------#
# Paint shop calculation (with cans, gallons, and mix)

def paint_shop_calc(liters):
    # Only cans
    cans = int(liters / 18)
    if liters % 18 != 0:
        cans += 1
    price_cans = cans * 80

    # Only gallons
    gallons = int(liters / 3.6)
    if liters % 3.6 != 0:
        gallons += 1
    price_gallons = gallons * 25

    # Mix of cans and gallons
    mix_cans = int(liters // 18)
    remainder = liters - (mix_cans * 18)
    mix_gallons = int(remainder / 3.6)
    if remainder % 3.6 != 0:
        mix_gallons += 1
    mix_total_price = (mix_cans * 80) + (mix_gallons * 25)

    print(f'''
Total liters needed: {liters:.1f}L
Cans only: {cans} - Price: R$ {price_cans:.2f}
Gallons only: {gallons} - Price: R$ {price_gallons:.2f}
Mix: {mix_cans} cans and {mix_gallons} gallons = R$ {mix_total_price:.2f}
''')

area_to_paint = float(input('Area size in square meters: '))
liters = area_to_paint / 6 * 1.1  # 10% extra
paint_shop_calc(liters)

#---------------------------#
# Download time calculation

def download_time(file_mb, link_mbps):
    time_seconds = file_mb / (link_mbps / 8)
    time_minutes = time_seconds / 60
    print(f'''
Time to download the file: {time_minutes:.2f} minutes
''')

file_size = float(input('Enter the file size in MB: '))
link_speed = float(input('Enter the link speed in Mbps: '))
download_time(file_size, link_speed)

#---------------------------#
