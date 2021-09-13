x = 9
PrimeTarget = 10001

PrimeList = [2, 3, 5, 7]

def check_prime(guess, primes):
    for prime_no in primes:
        if guess % prime_no == 0:
            return False

    return True

while len(PrimeList) < PrimeTarget:
    if check_prime(x, PrimeList):
        PrimeList.append(x)

    x += 2

print(x)
print(PrimeList)







list_for_home_work = []

for i in range(1001):
    list_for_home_work.append(i)

    for num in list_for_home_work:
        if num % 2 == 0:
            list_for_home_work.pop()

for i in range(len(list_for_home_work)):
    list_for_home_work[i] = list_for_home_work[i] ** 3

sum = 0
temporary_num = 0
exit_num = 0


for num_1 in list_for_home_work:
    temporary_list = list(str(num_1))
    print(temporary_list)

    for val_2 in temporary_list:
        temporary_num += int(val_2)
    print()
    if temporary_num % 7 == 0:
        sum += temporary_num


    exit_num += sum




for i in range(len(list_for_home_work)):
    list_for_home_work[i] += 17

sum = 0
temporary_num = 0
exit_num = 0

for num in list_for_home_work:
    temporary_list = list(str(num))

    for val_2 in temporary_list:
        temporary_num += int(val_2)

    if temporary_num % 7 == 0:
        sum += temporary_num
