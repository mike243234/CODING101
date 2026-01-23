sex = input("Type your biological sex:")
hgb = int(input("Type your hgb value:"))
def women_notify():
    if hgb < 117:
        print("Your hemoglobin is low ")
    elif 117 <= hgb <= 155:
        print("your hemoglobin is normal ")
    else :
        print("your hemoglobin is high")
def man_notify():
    if hgb < 134:
        print("Your hemoglobin is low ")
    elif 134 <= hgb <= 167:
        print("your hemoglobin is normal ")
    else:
        print("your hemoglobin is high")
if sex =="women":
    women_notify()
else:
    man_notify()