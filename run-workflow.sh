gh workflow run transform.yml

gh run list --workflow transform.yml

id=$(gh run list --workflow transform.yml  --json databaseId |  jq '.[0].databaseId')

gh run watch $id
