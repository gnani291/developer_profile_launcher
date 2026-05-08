import webbrowser
import requests
import logging
import time
# logging configuration
logging.basicConfig(
    filename="developer_profile_launcher",
    level=logging.INFO,
    format="%(asctime)s-%(message)s"
)
# dictionaty of websites
websites={
    1:("github","https://github.com/gnani291"),
    2:("leetcode","https://leetcode.com/u/Tadiparthi_Gnaneswar/"),
    3:("linkedin","https://www.linkedin.com/in/gnaneswar-tadiparthi-75a2b2328/"),
    4:("youtube","https://www.youtube.com/"),
    5:("google","https://www.google.com/")
}
#function to open websites
def open_website(url,name):
    print(f"\n Opening{name}...")
    logging.info(f"Opening{name}")
    webbrowser.open(url)
#function to know status codes 
def check_status(url,name):
    print(f"\n checking{name} status...")

    try:
        start_time =time.time()
        response=requests.get(url) 
        end_time=time.time()
        response_time = round(end_time - start_time, 2)
        
    
        if response.status_code==200:
            print(f"{name} is ONLINE")
            print(f"status code:{response.status.code}")
            print(f"response_time:{response_time}seconds")

            logging.info(f"{name} ONLINE - {response.status_code}")

        else:
            print(f"{name} returned error code {response.status_code}")

            logging.warning(f"{name} ERROR - {response.status_code}")

    except Exception as e:
        print("Error:", e)
        logging.error(f"{name} FAILED - {e}")
# Main Program
while True:

    print("\n===== WEBSITE LAUNCHER =====")
    print("1. github")
    print("2. leetcode")
    print("3. linkedin")
    print("4.youtube")
    print("5. google")
    print("6.Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 6:
        print("Exiting program...")
        break

    elif choice in websites:

        name, url = websites[choice]

        open_website(url, name)

        check_status(url, name)

    else:
        print("Invalid choice")

        

                  


