import pyautogui, time

# pyautogui.displayMousePosition()

#chuong nghỉ tam 5s
time.sleep(5)

# vi tri click but chi
x = 253
y = 80
pyautogui.moveTo(x, y)
pyautogui.click()
# nhan chuot vao vi tri đó de chon but chi

# di chuyen chuot den vi tri
x1 = 200
y1 = 250
pyautogui.moveTo(x1, y1)
distance = 200
delta = 5

while distance > 0:
    pyautogui.drag(distance, 0, 0.2)
    pyautogui.drag(0, distance, 0.2)
    # distance -= delta
    pyautogui.drag(-distance, 0, 0.2)
    distance -= delta
    pyautogui.drag(0, -distance, 0.2)
