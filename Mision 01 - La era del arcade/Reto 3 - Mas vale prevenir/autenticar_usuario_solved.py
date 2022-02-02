def authenticateUser(user, password):
    try: return authorizedPasswords[authorizedUsers.index(user)] == password
    except ValueError: pass
    return False


authorizedUsers = ["Alejandro", "Emma", "Leo", "Valeria", "Alvaro", "Daniela", "Manuel", "Alba", "Adrian", "Sara", "David",
                   "Carla", "Mario", "Carmen", "Diego", "Noa", "Enzo", "Claudia", "Marco", "Valentina", "Javier", "Alma",
                   "Marcos", "Vega", "Izan", "Ana", "Antonio", "Olivia", "Bruno", "Lola", "Sergio", "Chloe", "Alex", "Elena",
                   "Miguel", "Aitana", "Carlos", "Lara", "Marc", "Marta"]
authorizedPasswords = ["6589ab27", "fg_890**", "bpKm7811", "01234567", "ma22_89^5", "12az<<39", "<5-P4444", "2@#%ppLO", "1225_ter",
                       "ker-l889", "lurieg74", "u45<_'¡1", "aanz::41", "15cdz^77", "fdsiucny", "2w98asqw", "2nui89$$", "¡'9087qq",
                       "xc2a5r65", "r249864k", "26498__;", "w89d42ce", "w9y4245r", "<<>881s3", "q9w8t499", "mmmmmmmm", "a1f552()",
                       "w2ce7yrg", "5y96v42f", "+9q4hg53", "vvLIU529", "PPPP8571", "g86ae7QQ", "y68tj41i", "weq4fw6g", "7er8dtn1",
                       "maltisn5", "b2l9d544", "wn454j8a", "ngf5tr*4"]


if __name__ == "__main__":
    userInput = input()
    user, password = userInput.split(",")
    if authenticateUser(user, password):
        print("succeed")
    else:
        print("failed")
