af = int(input("Grunnfarge:\n"))
bf = int(input("Målfarge:\n"))
ratiob = float(input("Andel målfarge:\n"))
ratioa = 1.0 - ratiob

af0 = af // 1000000
af1 = (af - af0 * 1000000) // 1000
af2 = (af - af0 * 1000000 - af1 * 1000) // 1

bf0 = bf // 1000000
bf1 = (bf - bf0 * 1000000) // 1000
bf2 = (bf - bf0 * 1000000 - bf1 * 1000) // 1

f0 = round(((af0 * ratioa)+(bf0 * ratiob))) * 1000000
f1 = round(((af1 * ratioa)+(bf1 * ratiob))) * 1000
f2 = round(((af2 * ratioa)+(bf2 * ratiob)))

print(f0 + f1 + f2)



