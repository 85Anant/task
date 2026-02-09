def log_daily_goal():
    name = input("what's your name? ")
    goal = input("what's your daily goal? ")
    
    with open("journal.txt", "a") as file:
        file.write(f"{name}: {goal}\n")
        
if __name__ == "__main__":
    for _ in range(3):
        log_daily_goal()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        