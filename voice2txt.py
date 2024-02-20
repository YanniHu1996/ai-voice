import requests
import json
import os
import argparse

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

parser = argparse.ArgumentParser()
parser.add_argument("command", help="create or check")
parser.add_argument("--speech_url", help="Speech URL")
parser.add_argument("--task_id", help="Task ID")

args = parser.parse_args()


def main():
    if args.command == "create":
        create_task(args.speech_url)
    elif args.command == "check":
        check_task(args.task_id)
    else:
        print("Please specify a command")


def create_task(speech_url):
    url = (
        "https://aip.baidubce.com/rpc/2.0/aasr/v1/create?access_token="
        + get_access_token()
    )

    payload = json.dumps(
        {
            "speech_url": speech_url,
            "format": "mp3",
            "pid": 80001,
            "rate": 16000,
        }
    )
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    # {"log_id":17083226624200321,"task_status":"Created","task_id":"65d2ef66679f6f0001cb5d2b"}
    print(response.text)


def check_task(task_id):
    url = (
        "https://aip.baidubce.com/rpc/2.0/aasr/v1/query?access_token="
        + get_access_token()
    )

    payload = json.dumps({"task_ids": [task_id]})
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    # {
    #     "log_id": "17083973508265543",
    #     "tasks_info": [
    #         {
    #             "task_status": "Failure",
    #             "task_result": {"err_msg": "", "err_no": 2},
    #             "task_id": "65d2ef66679f6f0001cb5d2b",
    #         }
    #     ],
    # }
    print(response.text)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": SECRET_KEY,
    }
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == "__main__":
    main()
