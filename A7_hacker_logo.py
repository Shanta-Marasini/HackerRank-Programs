t = int(input(''))
a = 'H'
for i in range(t):
    print((a * i).rjust(t - 1) + a + (a * i).ljust(t - 1))

# Top Pillars
for i in range(t + 1):
    print((a * t).center(t * 2) +
          (a * t).center(t * 6))

# Middle Belt
for i in range((t + 1) // 2):
    print((a * t * 5).center(t * 6))

# Bottom Pillars
for i in range(t + 1):
    print((a * t).center(t * 2) +
          (a * t).center(t * 6))

# Bottom Cone
for i in range(t):
    print(((a * (t - i - 1)).rjust(t) + a +
           (a * (t - i - 1)).ljust(t)).rjust(t * 6))