from datetime import datetime

# format()
print('{:>100}'.format('Prawo'))
print('{:^100}'.format('Środek'))
print('{:_^100}'.format('Środek z wypełnieniem'))
print('{:32.14}'.format('Konstantynopolitańczykowianeczka'))
print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.now()))

# f-string
print(f"{'Prawo':>100}")
print(f"{'Środek':^100}")
print(f"{'Środek z wypełnieniem':_^100}")
print(f"{'Konstantynopolitańczykowianeczka':32.14}")
print(f"{datetime.now():%Y-%m-%d %H:%M:%S}")
