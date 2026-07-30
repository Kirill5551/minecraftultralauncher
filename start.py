import os
try:
    import questionary,subprocess,requests,sys,time,cloudscraper
except Exception:
    print("Установка библиотек...")
    os.system("pip install questionary requests cloudscraper")
    import questionary,subprocess,requests,sys,time,cloudscraper
current_dir=os.path.dirname(os.path.abspath(sys.argv[0]))
api_url="https://fill.papermc.io/v3"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*"
}
start=False
eula=True
proxy=False
eulas="Нет"
plugins=0
ram=0
for item in os.listdir():
    if item.endswith(".jar"):
        start=item
coreselector=[
    "[Серверное ядро] Paper (1.7.10-26.2)",
    "[Серверное ядро] Folia (1.19.4-26.2)",
    "[Прокси ядро] Velocity (все версии майна)",
    "[Прокси ядро] Waterfall (1.11-1.21)",
    "[Прокси ядро] Travertine (1.12-1.16)"
]
paperselector=[
    "[STABLE] 26.2","[STABLE] 26.1.2","[ALPHA] 26.1.1",
    "[STABLE] 1.21.11","[STABLE] 1.21.10","[ALPHA] 1.21.9",
    "[STABLE] 1.21.8","[STABLE] 1.21.7","[STABLE] 1.21.6",
    "[ALPHA] 1.21.5","[STABLE] 1.21.4","[STABLE] 1.21.3",
    "[STABLE] 1.21.1","[STABLE] 1.21",
    "[STABLE] 1.20.6","[ALPHA] 1.20.5","[STABLE] 1.20.4",
    "[STABLE] 1.20.2","[STABLE] 1.20.1","[STABLE] 1.20",
    "[STABLE] 1.19.4","[STABLE] 1.19.3","[STABLE] 1.19.2",
    "[STABLE] 1.19.1","[STABLE] 1.19",
    "[STABLE] 1.18.2","[STABLE] 1.18.1","[ALPHA] 1.18",
    "[STABLE] 1.17.1","[STABLE] 1.17",
    "[STABLE] 1.16.5","[STABLE] 1.16.4","[STABLE] 1.16.3",
    "[STABLE] 1.16.2","[STABLE] 1.16.1",
    "[STABLE] 1.15.2","[STABLE] 1.15.1","[STABLE] 1.15",
    "[STABLE] 1.14.4","[STABLE] 1.14.3","[STABLE] 1.14.2",
    "[STABLE] 1.14.1","[STABLE] 1.14",
    "[STABLE] 1.13.2","[STABLE] 1.13.1",
    "[STABLE] 1.13","[STABLE] 1.13-pre7",
    "[STABLE] 1.12.2","[STABLE] 1.12.1","[STABLE] 1.12",
    "[STABLE] 1.11.2","[STABLE] 1.10.2","[STABLE] 1.9.4",
    "[STABLE] 1.8.8","[STABLE] 1.7.10",
]
foliaselector=[
    "[BETA] 26.2","[STABLE] 26.1.2",
    "[STABLE] 1.21.11","[STABLE] 1.21.8","[STABLE] 1.21.6",
    "[ALPHA] 1.21.5","[ALPHA] 1.21.4","[ALPHA] 1.20.6",
    "[ALPHA] 1.20.4","[ALPHA] 1.20.1","[ALPHA] 1.19.4"
]
velocityselector=[
    "[STABLE] 4.0.0",
    "[RECOMMENDED] 3.5.1","[STABLE] 3.4.0","[STABLE] 3.1.1",
    "[STABLE] 3.1.0","[STABLE] 1.1.9","[STABLE] 1.0.10"
]
waterfallselector=[
    "[STABLE] 1.21","[STABLE] 1.20","[STABLE] 1.19",
    "[STABLE] 1.18","[STABLE] 1.17","[STABLE] 1.16",
    "[STABLE] 1.15","[STABLE] 1.14","[STABLE] 1.13",
    "[STABLE] 1.12","[STABLE] 1.11"
]
travertineselector=[
    "[STABLE] 1.16","[STABLE] 1.15","[STABLE] 1.14",
    "[STABLE] 1.13","[STABLE] 1.12"
]
actionselector=[
    "Запустить сервер",
    "Посмотреть логи",
    "Удалить ядро"
]
selector=["Да","Нет"]
os.system("cls")
if start:
    started=False
    while not started:
        print("Панель управления сервером")
        action=questionary.select("Выберите действие:", choices=actionselector).ask()
        if "З" in action:
            started=True
            try:
                for item in os.listdir():
                    if item.endswith("plugins"):
                        for p_item in os.listdir("plugins"):
                            if p_item.endswith(".jar"):
                                plugins += 1
                print(f"Обнаружено {plugins} плагинов.")
                while ram < 1:
                    ram=int(input("Сколько памяти выделить?: ГБ"))
                    if ram < 1:
                        print("Пожалуйста, выберите правильное количество памяти в ГБ для выделения.")
                os.system("cls")
                print(f"Ядро: {start} | Выделено {ram} ГБ")
            except Exception:
                print("Не удалось подготовиться к запуску.")
                os.system("pause")
                os.system("cls")
            try:
                os.system(f"java -Xms1G -Xmx{ram}G -jar {start} nogui")
                print("Сервер был остановлен или крашнут.")
                os.system("pause")
                os.system("cls")
            except Exception:
                print("Не удалось запустить сервер.")
                os.system("pause")
                os.system("cls")
        if "П" in action:
            try:
                print("Содержимое файла latest.log:")
                count=0
                with open('logs/latest.log','r',encoding='utf-8') as file:
                    for line in file:
                        count += 1
                        print(f"{count}. {line.rstrip()}")
                os.system("pause")
                os.system("cls")
            except Exception:
                print("latest.log не существует.")
                os.system("pause")
                os.system("cls")
        if "У" in action:
            confirm=questionary.select("Вы действительно хотите удалить ядро?", choices=selector).ask()
            if confirm=="Да":
                try:
                    os.remove(start)
                    print("Ядро удалено.")
                    os.system("pause")
                    exit()
                except Exception:
                    print("Недостаточно прав или файл не существует")
                    os.system("pause")
                os.system("cls")
else:
    print("Ядро не установлено.")
    os.system("pause")
    os.system("cls")
    print("Выберите ядро которое хотите установить:")
    choice=questionary.select("Выберите:", choices=coreselector).ask()
    print("Выберите версию ядра:")
    if "P" in choice:
        version=questionary.select("Выберите:", choices=paperselector).ask()
    if "F" in choice:
        version=questionary.select("Выберите:", choices=foliaselector).ask()
    if "V" in choice:
        version=questionary.select("Выберите:", choices=velocityselector).ask()
    if "W" in choice:
        version=questionary.select("Выберите:", choices=waterfallselector).ask()
    if "T" in choice:
        version=questionary.select("Выберите:", choices=travertineselector).ask()
    choice=choice.replace("[Серверное ядро]","").replace("[Прокси ядро]","").split(" ")[1].lower()
    if isinstance(version, list):
        version=version[-1]
    elif " " in str(version):
        version=str(version).split(" ")[-1]
    print(f"Поиск {choice}-{version}...")
    try:
        scraper=cloudscraper.create_scraper(
            browser={'browser':'chrome','platform':'windows','desktop': True}
        )
        download_url=""
        download_name=""
        version_url=f"{api_url}/projects/{choice}/versions/{version}"
        response=scraper.get(version_url,headers=headers)
        if response.status_code==200:
            builds=response.json().get("builds", [])
            if not builds:
                print(f"Ошибка: Для {choice}-{version} не найдено доступных сборок.")
            else:
                latest_build=builds[-1]
                if isinstance(latest_build, dict):
                    latest_build=latest_build.get("build", latest_build.get("id"))
                build_url=f"{version_url}/builds/{latest_build}"
                build_response=scraper.get(build_url,headers=headers)
                if build_response.status_code==200:
                    build_data=build_response.json()
                    downloads_data=build_data.get("downloads", {})
                    download_key=""
                    download_name=""
                    if "application" in downloads_data:
                        download_key="application"
                        download_name=downloads_data["application"].get("name","")
                    elif "bootstrap" in downloads_data:
                        download_key="bootstrap"
                        download_name=downloads_data["bootstrap"].get("name","")
                    else:
                        for key, val in downloads_data.items():
                            if isinstance(val, dict) and "name" in val:
                                download_key=key
                                download_name=val["name"]
                                break
                    if not download_key:
                        print("Ошибка: API v3 не предоставило конфигурацию файлов.")
                        os.system("pause")
                        exit()
                    candidate_urls=[]
                    file_info=downloads_data.get(download_key, {})
                    if isinstance(file_info, dict):
                        for prop in ["url","download_url","link"]:
                            if prop in file_info:
                                candidate_urls.append(file_info[prop])
                    candidate_urls.append(f"{build_url}/downloads/{download_key}")
                    candidate_urls.append(f"{build_url}/downloads/{download_name}")
                    candidate_urls.append(f"https://api.papermc.io/v2/projects/{choice}/versions/{version}/builds/{latest_build}/downloads/{download_name}")
                    file_response=None
                    print(f"Скачивание {choice}-{version} (Билд {latest_build}: {download_name})...")
                    for url in candidate_urls:
                        if not url:
                            continue
                        if url.startswith("/"):
                            url=f"https://fill.papermc.io{url}"
                        try:
                            res=scraper.get(url,headers=headers, stream=True)
                            if res.status_code==200:
                                file_response=res
                                break
                        except Exception:
                            pass
                    if file_response and file_response.status_code==200:
                        file_path=os.path.join(current_dir, download_name)
                        with open(file_path,"wb") as f:
                            for chunk in file_response.iter_content(chunk_size=128):
                                f.write(chunk)
                        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                            print(f"\nЯдро успешно скачано в папку скрипта.")
                            if eula:
                                while eulas=="Нет":
                                    eulas=questionary.select("Вы согласны с eula?: ", choices=selector).ask()
                                    if eulas=="Нет":
                                        print("Пожалуйста, прочитайте EULA (https://minecraft.net) и согласитесь.")
                                with open("eula.txt","w",encoding="utf-8") as f:
                                    f.write("eula=true\n")
                                print("Сервер настроен.")
                        else:
                            print("Ошибка: Загруженный файл оказался пустым.")
                            if os.path.exists(file_path): os.remove(file_path)
                    else:
                        print(f"Ответ сервера: {downloads_data}")
    except Exception as e:
        print(f"Произошла ошибка при выполнении скрипта: {e}")
os.system("pause")