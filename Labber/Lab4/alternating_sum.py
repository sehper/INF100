def alternate_sign_sum(nums):
    total = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            total += nums[i]
        else:
            total -= nums[i]
    return total

def test_alternate_sign_sum():
    print('Tester alternate_sign_sum...', end=' ', flush=True)
    assert 3 == alternate_sign_sum([1, 2, 3, 4, 5])
    assert 30 == alternate_sign_sum([10, 20, 30, 40, 50])

    a = [-10, 20, -30, 40, -50]
    assert -150 == alternate_sign_sum(a)
    assert [-10, 20, -30, 40, -50] == a  # Sjekk at funksjon ikke er destruktiv
    print('OK')

test_alternate_sign_sum()