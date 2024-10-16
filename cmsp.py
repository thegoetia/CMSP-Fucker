import requests
import json
from colorama import init, Fore

init(autoreset=True)


ascii_art = rf"""{Fore.RED}
  ____ __  __ ____  ____    _____ _   _  ____ _  _______ ____  
 / ___|  \/  / ___||  _ \  |  ___| | | |/ ___| |/ / ____|  _ \ 
| |   | |\/| \___ \| |_) | | |_  | | | | |   | ' /|  _| | |_) |
| |___| |  | |___) |  __/  |  _| | |_| | |___| . \| |___|  _ < 
 \____|_|  |_|____/|_|     |_|    \___/ \____|_|\_\_____|_| \_\
"""

print(ascii_art)

base_url = "https://edusp-api.ip.tv/tms/task"
api_key = "API_KEY_AQUI"
headers = {
    "Sec-Ch-Ua-Platform": "Windows",
    "X-Dash-Version": "1.1.757",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Ch-Ua": 'Chromium";v="129", "Not=A?Brand";v="8"',
    "X-Api-Key": api_key,
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Origin": "https://cmsp.ip.tv",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=4, i"
}

def check_question(task_id, question_id):
    print(f"Verificando a questão {question_id} da tarefa {task_id}...")  
    url = f"{base_url}/{task_id}/question/{question_id}/correct"

    payload = {
        "answer": {
            "answer": {
                "0": False,
                "1": True,  
                "2": False,
                "3": False,
                "4": False
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        print("Score:", response_data.get('score', 'N/A'))
        print("Comentário:")
        if 'comment' in response_data:
            comment = response_data['comment']
           
            assertions = comment.split('<p><br></p>')
            for assertion in assertions:
              
                assertion_clean = assertion.replace('<p>', '').replace('</p>', '').strip()
                if assertion_clean:  
                    print(f"- {assertion_clean}")
    else:
        print(f"Erro ao verificar a questão: {response.status_code}, {response.text}")


task_id = input("Digite o ID da tarefa: ")
question_id = input("Digite o ID da questão: ")


check_question(task_id, question_id)
