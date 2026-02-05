raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"] 
unique_users = set(raw_logs)
print("is ID05 a unique user?", "ID05" in unique_users)
print("raw logs count:", len(raw_logs))
print("unique users count:", len(unique_users))
print("unique users:",unique_users)