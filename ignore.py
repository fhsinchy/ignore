from os import remove
from sys import argv, exit
from requests import Session, ConnectionError

def main():
    file_name = '.gitignore'
    args = argv[1:]
    if len(args) > 0:
        session = Session()

        argument = args[0]

        try:
            if argument == 'templates':
                response = session.get('https://api.github.com/gitignore/templates')

                for template in response.json():
                    print(template)
            
            else:
                argument = argument.capitalize()

                response = session.get(f"https://api.github.com/gitignore/templates/{argument}",
                                headers={ 'Accept': 'application/vnd.github+json' })
                
                if response.status_code == 404:
                    exit(f"NO TEMPLATE FOUND FOR: {argument}")

                try:
                    remove(file_name)
                except OSError:
                    pass

                with open(file_name, 'a', encoding='utf-8') as toc_file:
                    toc_file.write(response.json()['source'])
            
        except ConnectionError:
            exit("OOPS! COULDN'T CONNECT TO GITHUB.")
    else:
        exit('NO ARGUMENT PASSED.')

if __name__ == '__main__':
    main()