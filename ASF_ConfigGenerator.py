import os
import json

if __name__ == '__main__': 
    while True:
        accs = input("Введите имя файла с аккаунтами(с расширением): ")
        configtype = input("Введите имя файла любого вашего настроенного конфига(enter для выбора testconfig.json): ")

        if not os.path.exists(accs) or (not os.path.exists(configtype) and not os.path.exists('testconfig.json')):
            print("Файл аккаунтов или конфига ввёден неверно, попробуйте ещё раз.")
            continue
        break
    
    if configtype == '': configtype = 'testconfig.json'
    
    with open(configtype, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    with open(accs, 'r', encoding='utf-8') as f:
        accsdata = f.read().split('\n')
    
    for acc in accsdata:
        if acc == '':
            continue
        login, password = acc.split(':')[:2]
        
        config['SteamLogin'] = login.strip()
        config['SteamPassword'] = password.strip()

        with open(f'{login}.json', 'w', encoding='utf8') as f:
            json.dump(config, f, indent=4)
        
        print(f'{login}.json generated')
        
