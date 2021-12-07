'''An auto login tool for demoblaze.com/index.html'''
import webbot

def run_login(username, password, web):
    '''
        Run login will take in username, password, and browser object
        to log into the website.
    '''

    web.click(id="login2")
    web.implicitly_wait(.25)
    web.type(username , id='loginusername', classname='form-control')
    web.implicitly_wait(.10)
    web.type(password , id='loginpassword')
    web.implicitly_wait(.10)
    web.click('Log in')
    web.implicitly_wait(.10)

    #Try to click "log out", else close alert and go onto next login
    try:
        web.click('Log out')
    except:
        with open('log.txt', 'a', encoding = 'UTF-8') as logfile:
            alert = web.switch_to_alert()
            alert.accept()
            logfile.write(f"Log in unsuccessful: Username {username} | Password {password}")
    else:
        with open('log.txt', 'a', encoding = 'UTF-8') as logfile:
            logfile.write(f"Log in successful: Username {username} | Password {password}")

    return False

def main():
    '''
        Main, launch browser and load webpage.
    '''

    web = webbot.Browser()
    web.fullscreen_window()
    web.go_to('demoblaze.com/index.html')
    web.implicitly_wait(.5)

    #put names and passwords into a list of tuples
    n_and_p_list = []
    with open("names_and_pass.txt", 'r', encoding = 'UTF-8') as n_and_p_file:
        lines = n_and_p_file.readlines()
        for line in lines:
            split_info = line.split(" ")
            n_and_p_list.append((split_info[0], split_info[1]))

    for item in n_and_p_list:
        run_login(item[0], item[1], web)


    web.quit()

if __name__ == "__main__":
    main()
