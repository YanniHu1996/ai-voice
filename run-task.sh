result=$(python voice2txt.py create --speech_url https://yannihu1996.github.io/ai-voice/record/吴晨旭讲五行基础.mp3)

# {"log_id":17083226624200321,"task_status":"Created","task_id":"65d2ef66679f6f0001cb5d2b"}
log_id=$(echo $result | jq -r '.log_id')
task_id=$(echo $result | jq -r '.task_id')
task_status=$(echo $result | jq -r '.task_status')

content=''
content=$content"\n-Task ID: $task_id"
content=$content"\n-Task Status: $task_status"
content=$content"\n-Log ID: $log_id"
content=$content"\n-Speech URL: https://yannihu1996.github.io/ai-voice/record/吴晨旭讲五行基础.mp3"

echo $content

gh issue create -R YanniHu1996/ai-voice comment --title '吴晨旭讲五行基础' --body "$content"
