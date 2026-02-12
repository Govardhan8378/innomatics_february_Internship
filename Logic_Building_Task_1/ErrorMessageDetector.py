logs = ["INFO", "ERROR", "WARNING", "ERROR"]

error_count = 0

for i in logs:
    if i == "ERROR":
        error_count += 1

print("Total ERRORS:", error_count)
